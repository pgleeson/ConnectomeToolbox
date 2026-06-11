# -*- coding: utf-8 -*-

############################################################

#    A simple script to read the values in CElegansNeuronTables.xls.

#    This is one of a number of interchangeable "Readers" which can
#    be used to get connection data

############################################################

from cect import print_

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import (
    CHEMICAL_SYN_TYPE,
    ELECTRICAL_SYN_TYPE,
    OTHER_CHEMICAL_NT,
)

from xlrd import open_workbook
import os
import sys

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"

filename = "%sCElegansNeuronTables.xls" % spreadsheet_location


READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity. Note: legacy dataset (based on White_whole) used in the past in OpenWorm. <b>Only included here for reference! Do not use!</b>"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


class SpreadsheetDataReader(ConnectomeDataset):
    def __init__(self):
        ConnectomeDataset.__init__(self)

        print_("Initialising SpreadsheetDataReader...")

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

        neurons2muscles, muscles, muscle_conns = self.read_muscle_data()
        for conn in muscle_conns:
            self.add_connection_info(conn)

    def read_data(self, include_nonconnected_cells=False):
        cells = []
        conns = []
        # reading the NeuronConnectFormatted.xls file if neuron_connect = True
        neuron_connect = False
        if neuron_connect:
            """
            filename = "%sNeuronConnectFormatted.xlsx" % spreadsheet_location
            rb = open_workbook(filename)
            print_("Opened the Excel file: " + filename)

            for row in range(1, rb.sheet_by_index(0).nrows):
                pre = str(rb.sheet_by_index(0).cell(row, 0).value)
                post = str(rb.sheet_by_index(0).cell(row, 1).value)
                syntype = rb.sheet_by_index(0).cell(row, 2).value
                num = int(rb.sheet_by_index(0).cell(row, 3).value)
                synclass = "Generic_GJ" if "EJ" in syntype else "Chemical_Synapse"

                self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if pre not in self.cells:
                    self.cells.append(pre)
                if post not in self.cells:
                    self.cells.append(post)

            return self.cells, self.conns"""

        else:
            rb = open_workbook(filename)

            sheet = 0
            print_("Opened sheet %i in Excel file: %s" % (sheet, filename))

            for row in range(1, rb.sheet_by_index(sheet).nrows):
                pre = str(rb.sheet_by_index(0).cell(row, 0).value)
                post = str(rb.sheet_by_index(0).cell(row, 1).value)
                syntype_here = rb.sheet_by_index(0).cell(row, 2).value
                if syntype_here == "Generic_GJ":
                    syntype = ELECTRICAL_SYN_TYPE
                else:
                    syntype = CHEMICAL_SYN_TYPE
                num = int(rb.sheet_by_index(0).cell(row, 3).value)
                synclass = rb.sheet_by_index(0).cell(row, 4).value

                if synclass == "Octapamine":
                    synclass = "Octopamine"

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

            if include_nonconnected_cells:
                from cect.Cells import PREFERRED_HERM_NEURON_NAMES

                for c in PREFERRED_HERM_NEURON_NAMES:
                    if c not in cells:
                        cells.append(c)

        return cells, conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        filename = "%sCElegansNeuronTables.xls" % spreadsheet_location
        rb = open_workbook(filename)

        sheet = 1
        print_("Opened sheet %i in Excel file: %s" % (sheet, filename))

        sheet = rb.sheet_by_index(sheet)

        for row in range(1, sheet.nrows):
            pre = str(sheet.cell(row, 0).value)
            post = str(sheet.cell(row, 1).value)
            syntype = CHEMICAL_SYN_TYPE
            num = int(sheet.cell(row, 2).value)
            synclass = (
                sheet.cell(row, 3)
                .value.replace(", ", "_")
                .replace(" ", "_")
                .replace(",", "plus")
            )

            if synclass == "":
                synclass = OTHER_CHEMICAL_NT
            if synclass == "FRMFemide":
                synclass = "FMRFamide"

            conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
            if pre not in neurons:
                neurons.append(pre)
            if post not in muscles:
                muscles.append(post)

        return neurons, muscles, conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("SpreadsheetDataReader"))
    else:
        return SpreadsheetDataReader()


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


def main():
    my_instance = get_instance()
    print("Analysing...")

    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    if "-nogui" not in sys.argv:
        # my_instance.connection_number_plot("OtherChemicalNT")

        from cect.ConnectomeView import RAW_VIEW as view

        """
        from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
        from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
       
        # from cect.ConnectomeView import SOCIAL_VIEW as view
        from cect.ConnectomeView import LOCOMOTION_2_VIEW as view"""

        print("--- Using view: %s" % view)
        cds2 = my_instance.get_connectome_view(view)
        print(cds2.summary())

        # fig = cds2.to_plotly_hive_plot_fig(list(view.synclass_sets.keys())[0], view)

        synclass = list(view.synclass_sets.keys())[0]
        synclass = "GABA"
        synclass = "OtherChemicalNT"

        # fig = cds2.to_plotly_graph_fig(synclass, view)
        fig = cds2.to_plotly_hive_plot_fig(synclass, view)

        import plotly.io as pio

        pio.renderers.default = "browser"

        fig.show()


if __name__ == "__main__":
    main()
