# Validation status of Data Readers

## WhiteEtAl1986

Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

The primary source of this data is https://www.wormatlas.org/neuronalwiring.html, and the []

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_A_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_A_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_L4_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_L4_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_whole_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_whole_expected_data.yaml'



## VarshneyEtAl2011

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//VarshneyDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//VarshneyDataReader_expected_data.yaml'



## BentleyEtAl2016

TODO...




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasMAReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasMAReader_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasPepReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasPepReader_expected_data.yaml'



## CookEtAl2019

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019HermDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019HermDataReader_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019MaleDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019MaleDataReader_expected_data.yaml'



## CookEtAl2020

Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).

The connectivity data was released in 2 CSV files in the supplementary information for that paper:

- [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) described as "Complete edge list for pharyngeal reconstruction."

- [cne24932-sup-0005-Supinfo5.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0005-Supinfo5.csv) described as "Inferred gap junction connectivity between end-organs". These connections have been included and some of these tested below also. 

These files were opened in Apple Numbers, and the weights (numbers of connections between pairs of cells, electrical or chemical) were read off, to provide checks listed below. 


### Validation tests for Cook2020DataReader (Chemical synaptic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 3 | Yes |
| I1R | I2L | 1 | Yes |
| RIPL | pm3VL | 4 | Yes |

### Validation tests for Cook2020DataReader (Electrical connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| e2DR | e3D | 2 | Yes |
| g1AL | M3L | 2 | Yes |
| pm1 | pm2VL | 3 | Yes |
| mc1V | pm3VL | 3 | Yes |
| mc3V | pm7VL | 3 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_



## BrittinEtAl2021

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//BrittinDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//BrittinDataReader_expected_data.yaml'



## WitvlietEtAl2021

Data on neuronal connectivity at different developmental stages of C. elegans from: Connectomes across development reveal principles of brain maturation
[Witvliet et al. 2021](https://www.nature.com/articles/s41586-021-03778-8), Nature 




### Validation tests for WitvlietDataReader1 (Chemical synaptic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| PVCL | SIAVL | 2 | Yes |
| AINR | AUAL | 2 | Yes |
| RIAL | RMDVR | 6 | Yes |
| URBR | IL1R | 1 | Yes |

### Validation tests for WitvlietDataReader1 (Electrical connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASHL | ADAL | 9 | Yes |
| RMDR | SMDVR | 1 | Yes |
| IL1R | IL1VR | 2 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader2_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader2_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader3_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader3_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader4_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader4_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader5_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader5_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader6_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader6_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader7_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader7_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader8_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader8_expected_data.yaml'



## RandiEtAl2023

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasFuncReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasFuncReader_expected_data.yaml'



## RipollSanchezEtAl2023

Data on neuropeptidergic signalling has been taken from: Ripoll-Sánchez et al. 2023, The neuropeptidergic connectome of C. elegans. [Neuron, Volume 111, Issue 22, 2023, Pages 3570-3589.e5](https://doi.org/10.1016/j.neuron.2023.09.043). 

There is a GitHub repository referenced in the paper: https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome. There are 3 different models used for the neuropeptidergic connectome (short-, medium- and long-range), and the following files have been used in Connectome Toolbox as the source of these models:

- [01022024_neuropeptide_connectome_short_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_short_range_model.csv)
- [01022024_neuropeptide_connectome_mid_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_mid_range_model.csv)
- [01022024_neuropeptide_connectome_long_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_long_range_model.csv)

For each of these CSV files, the file was opened in Apple Numbers, and the weights (numbers of matched peptides expressed in pre cell with corresponding receptor in post cell) read off, to provide checks listed below. 


### Validation tests for RipollSanchezShortRangeReader (Peptidergic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I3 | I5 | 3 | Yes |
| URBL | RMDDL | 4 | Yes |
| RIVR | HSNL | 6 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_




### Validation tests for RipollSanchezMidRangeReader (Peptidergic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| PVR | I3 | 6 | Yes |
| SABVL | VC1 | 1 | Yes |
| RIR | AVKR | 5 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_




### Validation tests for RipollSanchezLongRangeReader (Peptidergic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I3 | I5 | 3 | Yes |
| URBL | RMDDL | 4 | Yes |
| RIVR | HSNL | 6 | Yes |
| PVR | I3 | 6 | Yes |
| SABVL | VC1 | 1 | Yes |
| RIR | AVKR | 5 | Yes |
| VC4 | I4 | 1 | Yes |
| ALA | HSNR | 11 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_



## YimEtAl2024

Data on the dauer connectivity was obtained from the supplementary information of: Yim et al. 2024, Comparative connectomics of dauer reveals developmental plasticity
[Nature Communications, 15:1546](https://www.nature.com/articles/s41467-024-45943-3).

Supplementary Data 3 links to file [41467_2024_45943_MOESM6_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM6_ESM.xlsx).

This file has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM6_ESM.xlsx).

### Contactome based/non-normalised data

The spreadsheet above contained a sheet named "Dauer", from where the values for the contact area of connections were read. 
This file was opened in Excel and weights of selected connections were visually read from the cells, noting the pre and post cells and added to the connection test yaml file. 

### Normalised data

The spreadsheet above contained a sheet named "Dauer_normalized", from where the values for the "normalized" connections were read. 
This file was opened in Excel and weights of selected connections were visually read from the cells, noting the pre and post cells and added to the connection test yaml file. 


### Validation tests for Yim2024NonNormDataReader (Contact connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIH | CEPshDL | 7464.984227 | Yes |
| PVNL | ALMR | 97686.4 | Yes |
| URYDR | URADR | 33663.09403 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_




### Validation tests for Yim2024DataReader (Chemical synaptic connections)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | AFDR | 0.428024049927915 | Yes |
| SMBDL | RMED | 6.01978135910464 | Yes |
| ASHL | RIPL | 1.20804164634321 | Yes |

_Validation PASSED on 2026-04-16 with cect v0.3.1_



## WangEtAl2025

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024HermDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024HermDataReader_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024MaleDataReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024MaleDataReader_expected_data.yaml'



