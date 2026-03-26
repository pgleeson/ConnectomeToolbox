import modelspec
from modelspec import field, instance_of
from modelspec.base_types import Base
from typing import List
import yaml


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


if __name__ == "__main__":
    yim_data = ReaderExpectedData(reader="YIM")

    chem_conns = ConnectionList(
        synapse="chemical", comment="Data visually read in from xx.xlsx"
    )
    chem_conns.connections.append(Connection(pre="AVAL", post="AVAR", weight=0.5))
    chem_conns.connections.append(Connection(pre="AVAL", post="AVAL", weight=0.5))

    yim_data.connection_lists.append(chem_conns)

    with open("yim_expected_data.yaml", "w") as f:
        yaml.dump(yim_data.to_dict(), f, default_flow_style=False)
