############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

from cect.readers.WormNeuroAtlasExtSynReader import WormNeuroAtlasExtSynReader
from cect.Neurotransmitters import PEPTIDERGIC_SYN_CLASS
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import logging
import sys

NAME = "Bentley2016_PEPwna"

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on peptidergic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WormNeuroAtlasExtSynReader`` to load data on peptidergic connectivity using the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**

    Returns:
        (WormNeuroAtlasExtSynReader): The initialised connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        try:
            return WormNeuroAtlasExtSynReader(PEPTIDERGIC_SYN_CLASS)
        except Exception as e:
            print(
                "Problem loading WormNeuroAtlas data. Can be caused by WormBase url not working. Defaulting to loading from cache... Issue: %s"
                % str(e)
            )
            return get_instance(from_cache=True)


if __name__ == "__main__":
    my_instance = get_instance(from_cache=False)
    syn_class_to_test = PEPTIDERGIC_SYN_CLASS

    cells, neuron_conns = my_instance._read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["AIAL"]

    for cell in to_test:
        # my_instance.atlas.all_about(cell)

        print(
            "Pep conns from %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_from(
                            cell, syn_class_to_test, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

        print(
            "Pep conns to %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_to(
                            cell, syn_class_to_test, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

    if "-nogui" not in sys.argv:
        # from cect.ConnectomeView import NEURONS_VIEW as view
        from cect.ConnectomeView import RAW_VIEW as view
        # from cect.ConnectomeView import LOCOMOTION_2_VIEW as view
        # from cect.ConnectomeView import ESCAPE_VIEW as view
        # from cect.ConnectomeView import PHARYNX_VIEW as view

        # from cect.ConnectomeView import SOCIAL_VIEW as view
        # from cect.ConnectomeView import SOCIAL_VIEW as view
        # from cect.ConnectomeView import COOK_FIG3_VIEW as view
        # from cect.ConnectomeView import BRAINMAP_VIEW as view
        # from cect.ConnectomeView import BRAINMAP_A_VIEW as view
        # from cect.ConnectomeView import PEP_HUBS_VIEW as view

        # from cect.readers.TestDataReader import get_instance

        # from cect.readers.BrittinDataReader import get_instance
        # from cect.readers.WitvlietDataReader8 import get_instance
        # from cect.readers.Cook2019HermReader import get_instance
        # from cect.readers.Yim2024DataReader import get_instance
        # from cect.readers.WormNeuroAtlasMAReader import get_instance
        # from cect.readers.Wang2024Reader import get_instance

        # synclass = "Acetylcholine"
        # synclass = "Chemical"
        # synclass = "Electrical"
        # synclass = "Contact"
        # from cect.readers.TestDataReader import get_instance

        synclass = PEPTIDERGIC_SYN_CLASS
        synclass = "Extrasynaptic"

        # synclass = "dopamine"

        cds = get_instance()

        print("--------------------------------")
        print(cds.summary())
        print("--------------------------------")
        print(cds.__class__.__name__)

        cds2 = cds.get_connectome_view(view)

        print(cds2.summary())

        print("Keys: %s, plotting: %s" % (view.synclass_sets, synclass))

        # fig = cds2.to_plotly_hive_plot_fig(synclass, view)

        # fig = cds2.to_plotly_graph_fig(synclass, view)
        # fig = cds2.to_plotly_graph_fig(synclass, view)
        fig, _ = cds2.to_plotly_matrix_fig("Extrasynaptic", view)
        # fig, info = cds2.to_plotly_matrix_fig(
        #    list(view.synclass_sets.keys())[0], view, symmetry=True
        # )
        # fig = cds2.to_plotly_matrix_fig(synclass, view)

        import plotly.io as pio

        pio.renderers.default = "browser"
        if "-nogui" not in sys.argv:
            fig.show()
