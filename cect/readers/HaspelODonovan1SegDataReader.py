from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT


from cect import print_
import os


# ruff: noqa: F401
from cect.readers.HaspelODonovanDataReader import WEIGHTS, ONE_SEG_CONN, filename

from cect.readers.HaspelODonovanDataReader import HaspelODonovanDataReader

NAME = "HaspelODonovan1Seg"

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity (one segment)"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)

DATASET_DESCRIPTION = "(ONE SEGMENT) A complete connectivity model for all 75 _C. elegans_ ventral cord motorneurons from Haspel and O'Donovan 2011, produced by identifying a repeating pattern in the empirically known anterior connections and extrapolating it into the posterior half of the animal where direct EM data were absent."


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        return HaspelODonovanDataReader(full_or_one_seg=ONE_SEG_CONN)


def main():
    my_instance = get_instance()

    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(
        cells, neuron_conns, neurons2muscles, muscles, muscle_conns, print_details_on=[]
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    cell = "DB1"
    syntype = "Generic_CS"
    conns = my_instance.get_connections_from(cell, syntype)
    print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")

    import numpy as np

    for syntype in my_instance.connections.keys():
        conn_array = my_instance.connections[syntype]
        print(
            f"\n === Connection array for synapse type {syntype} has shape: {conn_array.shape}"
        )
        nonzero = np.count_nonzero(conn_array)
        count_diagonal_entries = np.count_nonzero(np.diag(conn_array))
        is_symmetric = np.array_equal(conn_array, conn_array.T)
        sym_info = ""
        if is_symmetric:
            diagonal_sum = np.sum(np.diag(conn_array))
            unique_sum = (np.sum(conn_array) - diagonal_sum) / 2 + diagonal_sum

            sym_info = f"\nMatrix is symmetric with <b>{count_diagonal_entries + int((nonzero - count_diagonal_entries) / 2)}</b> unique pairs (total unique pair weight: <b>{unique_sum}</b>)<br/>"
        else:
            sym_info = "\nNOT symmetric"
        diag_info = (
            "<b>%s</b> nodes with self-connections<br/>" % count_diagonal_entries
            if count_diagonal_entries > 0
            else ""
        )
        print(
            f"<b>{nonzero}</b> non-zero entries<br/>{diag_info}{sym_info}Avg. weight: <b>{np.mean(conn_array[conn_array != 0])}</b><br/>Sum of weights: <b>{np.sum(conn_array)}</b>\n"
        )

        import sys

        if "-nogui" not in sys.argv:
            print(my_instance.summary())

            from cect.ConnectomeView import RAW_VIEW as view
            # from cect.ConnectomeView import NEURONS_VIEW as view

            cds2 = my_instance.get_connectome_view(view)

            print(cds2.summary())

            """
            fig = cds2.to_plotly_graph_fig(DOPAMINE, view)
            """

            fig, _ = cds2.to_plotly_matrix_fig(
                "Chemical",
                view,
            )
            import plotly.io as pio

            pio.renderers.default = "browser"
            import sys

            fig.show()


if __name__ == "__main__":
    main()
