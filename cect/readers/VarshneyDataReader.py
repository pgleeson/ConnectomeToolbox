from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import GENERIC_CHEM_SYN_CLASS, CHEMICAL_SYN_TYPE
from cect.Neurotransmitters import GENERIC_ELEC_SYN_CLASS, ELECTRICAL_SYN_TYPE

from openpyxl import load_workbook

import os

from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"
spreadsheet_name = "NeuronConnect.xlsx"  # has old name...
spreadsheet_name = "NeuronConnectFormatted.xlsx"
filename = "%s%s" % (spreadsheet_location, spreadsheet_name)

NAME = "Varshney"

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)

NMJ_ENDPOINT = "NMJ"

SEND_SYN = "S"
SEND_POLY_SYN = "Sp"
RECEIVE_SYN = "R"
RECEIVE_POLY_SYN = "Rp"

ELECT_JUNC_SYN = "EJ"


class VarshneyDataReader(ConnectomeDataset):
    """Reader for Varshney et al. 2011 connectivity dataset"""

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(
                conn,
                append_existing_connections=True,
                check_overwritten_connections=True,
                fail_on_any_repeated_connection=False,
            )

    def read_data(self):
        cells = []
        conns = []

        self.typed_conns = {"S": [], "Sp": [], "R": [], "Rp": [], "EJ": []}

        wb = load_workbook(filename)
        sheet = wb.worksheets[0]
        print_("Opened the Excel file: " + filename)

        for row in sheet.iter_rows(
            min_row=2, values_only=True
        ):  # Assuming data starts from the second row
            pre = str(row[0])
            post = str(row[1])

            if not post == NMJ_ENDPOINT:
                syntype_here = str(row[2])
                num = int(row[3])

                self.typed_conns[syntype_here].append(f"{pre}_{post}_{num}")

                synclass = (
                    GENERIC_ELEC_SYN_CLASS
                    if syntype_here == ELECT_JUNC_SYN
                    else GENERIC_CHEM_SYN_CLASS
                    if (syntype_here == SEND_POLY_SYN or syntype_here == SEND_SYN)
                    else None
                )
                if syntype_here == ELECT_JUNC_SYN:
                    syntype = ELECTRICAL_SYN_TYPE
                else:
                    syntype = CHEMICAL_SYN_TYPE

                if synclass is not None:
                    conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                    if pre not in cells:
                        cells.append(pre)
                    if post not in cells:
                        cells.append(post)
                else:
                    if not (
                        syntype_here == RECEIVE_SYN or syntype_here == RECEIVE_POLY_SYN
                    ):
                        raise ValueError(
                            f"Warning: Unrecognized synapse type '{syntype_here}' for connection {pre} -> {post} for {NAME}."
                        )

        for syn_type, conn_list in self.typed_conns.items():
            print_(
                f"  {syn_type}: {len(conn_list)} connections ({', '.join(conn_list[:5])}...) "
            )
        s_tot = len(self.typed_conns[SEND_SYN]) + len(self.typed_conns[SEND_POLY_SYN])
        r_tot = len(self.typed_conns[RECEIVE_SYN]) + len(
            self.typed_conns[RECEIVE_POLY_SYN]
        )
        print_(
            f"  Total chemical synapses: {s_tot} (send) + {r_tot} (receive) = {s_tot + r_tot}"
        )
        print_(f"  Total electrical synapses: {len(self.typed_conns[ELECT_JUNC_SYN])}")

        return cells, conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        return neurons, muscles, conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        return VarshneyDataReader()


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


def main():
    my_instance = get_instance()

    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    cell = "ADAL"
    syntype = "Generic_CS"
    conns = my_instance.get_connections_from(cell, syntype)
    print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main()
