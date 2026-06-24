Data from: The Multilayer Connectome of Caenorhabditis elegans, Bentley et al. 2016, [PLoS Comput Biol 12(12): e1005283](https://doi.org/10.1371/journal.pcbi.1005283)

Connectivity was originally released in supplementary information: [S1 Dataset](https://doi.org/10.1371/journal.pcbi.1005283.s004) ("Included are edge lists for monoamine and neuropeptide networks").

Data on the extrasynaptic connections was accessed using the [WormNeuroAtlas](https://github.com/francescorandi/wormneuroatlas) Python package in the WormNeuroAtlasMAReader for the DataReader.

For the validation tests below, specific connections between pre and postsynaptic cells were read out from the edgelist_MA.csv file in [S1 Dataset](https://doi.org/10.1371/journal.pcbi.1005283.s004) above and a weight of 1 was added to the connection test yaml file for these. 
