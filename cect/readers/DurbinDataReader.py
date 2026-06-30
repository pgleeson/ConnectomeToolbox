from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Cells import UNSPECIFIED_BODY_WALL_MUSCLE

from cect.Neurotransmitters import GENERIC_CHEM_SYN_CLASS, CHEMICAL_SYN_TYPE
from cect.Neurotransmitters import GENERIC_ELEC_SYN_CLASS, ELECTRICAL_SYN_TYPE


import os

from cect import print_

data_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"

txt_filename = "neurodata_fixed.txt"
filename = "%s%s" % (data_location, txt_filename)

NAME = "Durbin"

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


WEIGHTS = "Weights are... (TODO) "
N2U_ADULT = "N2U"
JSH_L4 = "JSH"

SEND_SYN = "Send"
SEND_POLY_SYN = "Send_joint"
SEND_ANY = "SEND"
RECEIVE_SYN = "Receive"
RECEIVE_POLY_SYN = "Receive_joint"
RECEIVE_ANY = "RECEIVE"

ELECT_JUNC_SYN = "Gap_junction"

NMJ_ENDPOINT = "mu_bod"


def _remove_leading_index_zero(cell):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if cell[:2] in ["VA", "VB", "VC", "VD", "DA", "DB", "DD", "AS"] and cell[
        -2:
    ].startswith("0"):
        return "%s%s" % (cell[:-2], cell[-1:])
    return cell


class DurbinDataReader(ConnectomeDataset):
    """Reader for Durbin connectivity dataset"""

    def __init__(
        self,
        worm_strain,
        include_nmj=True,
    ):
        ConnectomeDataset.__init__(self)

        self.typed_conns = {
            SEND_SYN: [],
            SEND_POLY_SYN: [],
            RECEIVE_SYN: [],
            RECEIVE_POLY_SYN: [],
            SEND_ANY: set(),
            RECEIVE_ANY: set(),
            ELECT_JUNC_SYN: [],
            NMJ_ENDPOINT: [],
        }

        self.include_nmj = include_nmj
        self.worm_strain = worm_strain
        cells, neuron_conns = self.read_data()

        for conn in neuron_conns:
            self.add_connection_info(
                conn,
                append_existing_connections=True,
                check_overwritten_connections=True,
                fail_on_any_repeated_connection=False,
            )

    def _check_valid_synapse_type(self, syn_type):
        if syn_type not in self.typed_conns:
            raise ValueError(
                f"Synapse type '{syn_type}' not recognized for {NAME}. Valid types are: {list(self.typed_conns.keys())}"
            )
        return syn_type

    def read_data(self):
        cells = []
        conns = []

        print_("Opening the text file: " + filename)

        for line in open(filename, "r"):
            if "#" in line:
                line = line.split("#")[0]
            if len(line.strip()) == 0:
                continue
            row = line.split()
            print_(f"Processing line: {row}")
            pre = str(row[0])
            post = str(row[1])

            pre = _remove_leading_index_zero(pre)
            post = _remove_leading_index_zero(post)

            if post == NMJ_ENDPOINT:
                post = UNSPECIFIED_BODY_WALL_MUSCLE

            syntype_here = self._check_valid_synapse_type(str(row[2]))

            worm_strain_here = str(row[3])

            if worm_strain_here != self.worm_strain:
                continue

            num = int(row[4])

            self.typed_conns[syntype_here].append(f"{pre}_{post}_{num}")
            if syntype_here in [SEND_SYN, SEND_POLY_SYN]:
                self.typed_conns[SEND_ANY].add(f"{pre}_{post}")
            elif syntype_here in [RECEIVE_SYN, RECEIVE_POLY_SYN]:
                self.typed_conns[RECEIVE_ANY].add(f"{pre}_{post}")

            if syntype_here != NMJ_ENDPOINT or self.include_nmj:
                synclass = (
                    GENERIC_ELEC_SYN_CLASS
                    if syntype_here == ELECT_JUNC_SYN
                    else GENERIC_CHEM_SYN_CLASS
                    if (syntype_here == SEND_POLY_SYN or syntype_here == SEND_SYN)
                    else GENERIC_CHEM_SYN_CLASS
                    if (syntype_here == NMJ_ENDPOINT)
                    else None
                )

                if syntype_here == ELECT_JUNC_SYN:
                    syntype = ELECTRICAL_SYN_TYPE
                else:
                    syntype = CHEMICAL_SYN_TYPE

                if synclass is not None:
                    conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                    """if syntype == ELECTRICAL_SYN_TYPE:
                        # Note: some electrical connections are only present in one direction in the file, but we will treat them as symmetric when read in
                        conns.append(ConnectionInfo(post, pre, num, syntype, synclass))
                        pass"""
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

        total = 0
        for syn_type, conn_list in self.typed_conns.items():
            total += len(conn_list)
            info = ""
            if syn_type in [SEND_SYN, SEND_POLY_SYN, RECEIVE_SYN, RECEIVE_POLY_SYN]:
                info = f"\t({', '.join(conn_list[:5])}..., {conn_list[-1]})"

            print_(
                f"  {syn_type}: {len(conn_list)} connections\t({len(set(conn_list))} unique) {info}"
            )

        print_(f"  Total: {total} connections (half: {total / 2})")

        s_tot = len(self.typed_conns[SEND_SYN]) + len(self.typed_conns[SEND_POLY_SYN])

        r_tot = len(self.typed_conns[RECEIVE_SYN]) + len(
            self.typed_conns[RECEIVE_POLY_SYN]
        )

        print_(
            f"  Total chemical synapses: {s_tot} (send) + {r_tot} (receive) = {s_tot + r_tot}"
        )
        gj = len(self.typed_conns[ELECT_JUNC_SYN])
        print_(f"  Total electrical synapses: {gj}, half: {gj / 2}")

        return cells, conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        return neurons, muscles, conns


def _get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        return DurbinDataReader(worm_strain=N2U_ADULT, include_nmj=True)


def main():
    my_instance = _get_instance()

    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(
        cells, neuron_conns, neurons2muscles, muscles, muscle_conns, print_details_on=[]
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    cell = "ADAR"
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


if __name__ == "__main__":
    main()
