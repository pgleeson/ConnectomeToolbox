# Reader for Cook et al 2019 data


from cect.readers.Cook2019DataReader import Cook2019DataReader
from cect.readers.Cook2019DataReader import HERMAPHRODITE

# ruff: noqa: F401
from cect.readers.Cook2019DataReader import WEIGHTS

from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections

import sys


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "Cook2019Herm"

DATASET_DESCRIPTION = "Chemical and electrical connectivity of the hermaphrodite from Cook et al 2019, including connections between neurons, muscles and other cells."


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``Cook2019DataReader`` to load data on hermaphrodite connectome

    Returns:
        (Cook2019DataReader): The initialized hermaphrodite connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("Cook2019HermReader"))
    else:
        return Cook2019DataReader(HERMAPHRODITE)


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity of hermaphrodite"""
    % get_dataset_source_on_github(Cook2019DataReader.filename.split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot("Acetylcholine")

    print(my_instance.summary())

    cells = ["M4"]
    syntypes = ["Generic_CS", "Generic_GJ"]

    for cell in cells:
        for syntype in syntypes:
            conns = my_instance.get_connections_from(cell, syntype)
            print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
            for c in sorted(conns.keys()):
                print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main1()
