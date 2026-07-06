Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](https://royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

As described on [WormAtlas](https://www.wormatlas.org/neuronalwiring.html), the primary structured dataset describing this connectivity is the **neurodata.txt** file which was compiled by Richard Durbin in his 1987 thesis. This (and the [Readme](https://www.wormatlas.org/neurodata_readme.txt) describing it) can be found [on WormAtlas](https://www.wormatlas.org/neurodata.txt). 

This file describes reconstructed connectivity for 2 animals: an N2U (adult hermaphrodite) and JSH (which Durbin described as an L4 male, it is now believed that this animal was an L4 hermaphrodite). This file been copied into our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata.txt).

However, an [updated version of this file](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata_updated.txt) was used in the DurbinDataReader in cect, as the following minor issues were found in the file, and thse were incorporated in the data source, as opposed to the Python reader, for clarity:

**Issue 1)** Line 2 in the original file (ADAL ADAR Gap_junction 1) was missing JSH or N2U, and so assuming N2U as "ADAL ADAR Gap_junction JSH 2" was already present.
**Issue 2)** While most gap junction connections contained both A->B and B->A connections, but some were missing the reverse connection. The missing connections at the top of the file.
**Issue 3)** One gap junction connection had a different weight for the A->B and B->A connections (RIML<->AVAR). Updated the weight to be the same for both directions, using the larger of the two weights.

The "White Whole" dataset is effectively the same as the Varshney et al. 2011 dataset, apart from also containing the connections to/from the pharynx. This dataset was obtained from the [WormNeuroAtlas source code](https://github.com/francescorandi/wormneuroatlas/blob/main/wormneuroatlas/data/aconnectome_white_1986_whole.csv), and copied to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/aconnectome_white_1986_whole.csv).
