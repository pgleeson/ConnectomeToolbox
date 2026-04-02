from cect import print_

from cect.Neurotransmitters import GENERIC_CHEM_SYN
from cect.Utils import get_connectome_dataset

import modelspec
from modelspec import field, instance_of
from modelspec.base_types import Base
from typing import List
import yaml
import sys

import unittest


class TestExpectedConnections(unittest.TestCase):
    MISMATCH = "Mismatch"

    def test_all(self):

        validation_md = "# Validation status of Data Readers\n\n"

        data_readers = ["Yim2024DataReader", "Cook2020DataReader"]
        data_readers = {
            "YimEtAl2024": ["Yim2024DataReader"],
            "CookEtAl2020": ["Cook2020DataReader"],
        }

        for data_set in data_readers:
            validation_md += f"## {data_set}\n\n"
            with open(__file__.replace("Validator.py", f"{data_set}.md"), "r") as f:
                validation_md += f.read() + "\n\n"

            for data_reader in data_readers[data_set]:
                print_(f"Validating reader: {data_reader}...")

                validation_md += f"### Validation tests for {data_reader}\n\n"
                report = self.load_and_check_expected_data(data_reader)
                validation_md += report + "\n\n"

        with open(
            __file__.replace("Validator.py", "../../docs/Validation.md"), "w"
        ) as f:
            f.write(validation_md)

        assert self.MISMATCH not in validation_md, (
            "Validation failed for some connections. See Validation.md for details."
        )

    def load_and_check_expected_data(self, data_reader):

        report = ""

        expected_data_folder = __file__.replace("Validator.py", "")
        expected_data_file = f"{expected_data_folder}/{data_reader}_expected_data.yaml"

        with open(expected_data_file, "r") as f:
            print_(
                f"Loading expected data for {data_reader} from {expected_data_file}..."
            )
            expected_data = ReaderExpectedData.from_yaml(f)

        self.assertIsInstance(expected_data, ReaderExpectedData)
        self.assertEqual(expected_data.reader, data_reader)

        data_reader_ref = data_reader.replace("DataReader", "")

        conn_dataset = get_connectome_dataset(data_reader_ref, from_cache=True)

        print_(conn_dataset.summary())

        for conn_list in expected_data.connection_lists:
            print_(f"Checking connection list: {conn_list}, {conn_list['synapse']}...")

            report += "| Pre      | Post | Expected weight | Match |\n|----------|------|-----------------|-------|\n"

            for conn in conn_list["connections"]:
                print_(f"Checking connection: {conn}...")
                w = conn_dataset.get_connection_weight(
                    conn["pre"], conn["post"], synclass=conn_list["synapse"]
                )
                self.assertIsNotNone(
                    w, f"Connection weight for {conn} should not be None"
                )
                match_info = "Yes" if w == conn["weight"] else f"{self.MISMATCH}: {w}"
                print_(match_info)
                report += f"| {conn['pre']} | {conn['post']} | {conn['weight']} | {match_info} |\n"

        return report


@modelspec.define
class Connection(Base):
    """
    A single connection between two cells.

    Args:
        pre: The pre-synaptic cell
        post: The post-synaptic cell
        weight: The weight of the connection, which could be the number of synapses or a normalized value.
    """

    pre: str = field(validator=instance_of(str))
    post: str = field(validator=instance_of(str))
    weight: float = field(validator=instance_of(float))


@modelspec.define
class ConnectionList(Base):
    """
    A model of a list of connections of a specific synapse type.

    Args:
        synapse: The type of synapse
        comment: A comment about how the data was found, e.g. taken from a spreadsheet
        connections: The list of connections of this type
    """

    synapse: str = field(validator=instance_of(str))
    comment: str = field(validator=instance_of(str))
    connections: List[Connection] = field(factory=list)


@modelspec.define
class ReaderExpectedData(Base):
    """
    A model of expected data for a specific reader.

    Args:
        reader: The name of the reader
        connection_lists: The list of connection lists for this reader
    """

    reader: str = field(validator=instance_of(str))
    connection_lists: List[ConnectionList] = field(factory=list)

    def get_connection_list_by_synapse(self, synapse_type):
        """
        Get the connection list for a specific synapse type.

        Args:
            synapse_type: The type of synapse to get the connection list for


        Returns:            The connection list for the specified synapse type, or None if not found.
        """
        for conn_list in self.connection_lists:
            if (
                isinstance(conn_list, dict)
                and "synapse" in conn_list
                and conn_list["synapse"] == synapse_type
            ):
                return conn_list
            if conn_list.synapse == synapse_type:
                return conn_list
        return None


def generate_reader_exp_data_obj(reader_name, source_files, additional_comment=""):
    """
    A function to generate a ReaderExpectedData object which will list expected data as visually extracted from a source file, e.g. an Excel spreadsheet.

    Args:
        reader_name: The name of the reader
        source_files: A dict of syn types vs paths to the source files

    Returns:
        A ReaderExpectedData object with the expected data for the reader.
    """
    # This is a placeholder implementation. In a real implementation, you would read the source files and extract the expected data.
    expected_data = ReaderExpectedData(reader=reader_name)

    for syn_type, source_file in source_files.items():
        chem_conns = ConnectionList(
            synapse=syn_type,
            comment=f"Data visually read in from {source_file}. {additional_comment}",
        )

    expected_data.connection_lists.append(chem_conns)

    return expected_data


if __name__ == "__main__":
    if "-test" in sys.argv:
        expected_data_folder = __file__.replace("Validator.py", "")

        yim_data = generate_reader_exp_data_obj(
            reader_name="Yim2024DataReader",
            source_files={GENERIC_CHEM_SYN: "41467_2024_45943_MOESM6_ESM.xlsx"},
            additional_comment='Normalized data is on tab/sheet "Dauer_normalized". Values were copied from the cells in Microsoft Excel',
        )

        chem_conns = yim_data.get_connection_list_by_synapse(GENERIC_CHEM_SYN)

        chem_conns.connections.append(
            Connection(pre="ADFR", post="AFDR", weight=0.428024049927915)
        )
        chem_conns.connections.append(
            Connection(pre="SMBDL", post="RMED", weight=6.01978135910464)
        )
        chem_conns.connections.append(
            Connection(pre="ASHL", post="RIPL", weight=1.20804164634321)
        )

        exp_data_file = f"{expected_data_folder}/{yim_data.reader}_expected_data.yaml"
        with open(exp_data_file, "w") as f:
            yaml.dump(yim_data.to_dict(), f, default_flow_style=False)

        print_(f"Expected data for YIM reader written to {exp_data_file}")

    else:
        unittest.main()
        sys.exit(0)
