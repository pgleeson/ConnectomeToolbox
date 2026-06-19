# Validation status of Data Readers

## WhiteEtAl1986

Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](https://royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

The primary source of this data is https://www.wormatlas.org/neuronalwiring.html, and the []

TODO...


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_A_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_A_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_L4_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_L4_expected_data.yaml'




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_whole_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//White_whole_expected_data.yaml'



## VarshneyEtAl2011

TODO...


The dataset...


### Validation tests for VarshneyDataReader 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AS5 | 3 | Yes |
| ADAL | AVBR | 7 | Yes |

Expected total weight of connections: 6394 (matches)

Expected number of nonzero connection weights: 2194 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 5 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 1031 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



## BentleyEtAl2016

Data from: The Multilayer Connectome of Caenorhabditis elegans, Bentley et al. 2016, [PLoS Comput Biol 12(12): e1005283](https://doi.org/10.1371/journal.pcbi.1005283)

Connectivity was originally released in supplementary information: [S1 Dataset](https://doi.org/10.1371/journal.pcbi.1005283.s004) ("Included are edge lists for monoamine and neuropeptide networks").

Data on the extrasynaptic connections was accessed using the [Worm Neuro Atlas](https://github.com/francescorandi/wormneuroatlas) package in the WormNeuroAtlasMAReader.








**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasMAReader_expected_data.yaml**: No such connectome dataset registered: Bentley2016_MA (or Bentley2016_MA)
Known datasets: ['White_A', 'White_L4', 'White_whole', 'Witvliet1', 'Witvliet2', 'Witvliet3', 'Witvliet4', 'Witvliet5', 'Witvliet6', 'Witvliet7', 'Witvliet8', 'Varshney', 'Cook2019Herm', 'Cook2019Male', 'Cook2020', 'Brittin2021', 'RipollSanchezShortRange', 'RipollSanchezMidRange', 'RipollSanchezLongRange', 'Yim2024', 'Yim2024NonNorm', 'Wang2024Herm', 'Wang2024Male']




**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasPepReader_expected_data.yaml**: [Errno 2] No such file or directory: '/Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasPepReader_expected_data.yaml'



## CookEtAl2019

Data was taken from: Cook et al. 2019, Whole-animal connectomes of both Caenorhabditis elegans sexes. [Nature 571, 63–71](https://doi.org/10.1038/s41586-019-1352-7).

Three spreadsheets with these connections have been identified:

1) Original Supplementary information 5

Connectivity matrices were released in the following supplementary information file with the publication: [41586_2019_1352_MOESM9_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/MediaObjects/41586_2019_1352_MOESM9_ESM.xlsx).

**Note:** there is a slight internal consistency issue this file - some of the male ray structural cells are named R1stL, R2stR, etc. ), but in other locations the names R1shL, R2shR, etc. are used.


2) WormWiring original adjacency matrices

On WormWiring (Emmons lab), there is a link: Original Connectome Adjacency Matrices (ref 1, SI5) [SI 5 Connectome adjacency matrices.xlsx](https://wormwiring.org/si/SI%205%20Connectome%20adjacency%20matrices.xlsx).

**Note:** there is a slight difference between this file and the original - some of the male ray structural cells R1stL, R2stR cells have been changed to R1shL, R2shR, etc. in this file.

3) WormWiring corrected adjacency matrices

There is also a file: Hermaphrodite and Male Connectomes (Adjacency Matrices), Adults (corrected July 2020) [[SI 5 Connectome adjacency matrices, corrected July 2020.xlsx](https://wormwiring.org/si/SI%205%20Connectome%20adjacency%20matrices,%20corrected%20July%202020.xlsx)].

The differences in this file are as follows: 

_Hermaphrodite gap junctions_
- Added: PVDL ↔ hmc: weight 400
- Added: PVDR ↔ hmc: weight 400
- Removed: BDUR ↔ PLMR: weight 23
- The following connections were not originally present in both directions (i.e. a fully symmetrical electrical connection was not present): 
    - DD06 ↔ PDB
    - ALA ↔ exc_gl
    - VA09 ↔ PVCR

_Male gap junctions_
- Added: DD1 ↔ MVL08: weight 2
- Removed: RIVR ↔ FLPL: weight 1
- The following connections were not originally present in both directions (i.e. a fully symmetrical electrical connection was not present): 
    - DD1 ↔ MVR08
    - R8AL ↔ R8BL
    - RIVL ↔ FLPL
    - VB6 ↔ VB7
    - VB7 ↔ VB5
    - MDR08 ↔ DD1
    
**In Connectome Toolbox, we use spreadsheet 3), and use R1stL, R2stR, etc., as these are the names used [on WormAtlas](https://www.wormatlas.org/male/rays/mainframe.htm#Celllist5).**

Additionally, we used **g1P**, not **g1p** for the name of this pharyngeal glial cell, as this is the form used in Cook et al. 2020, as well as on WormWiring. 

This file was opened in Excel and weights of selected connections were visually read from the cells on the specific sheets (e.g. hermaphrodite chemical, male gap jn symmetric), 
noting the pre and post cells and these added to the connection test yaml file, along with the total number of nonzero connections in each adjacency matrix as well as the total weights. 


### Validation tests for Cook2019HermReader 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 6 | Yes |
| SMBDL | SDQR | 18 | Yes |
| VC2 | PVT | 6 | Yes |
| DB4 | MDL13 | 4 | Yes |
| RIMR | MDL05 | 15 | Yes |
| M1 | g1P | 5 | Yes |
| I6 | g1P | 2 | Yes |

Expected total weight of connections: 28113 (matches)

Expected number of nonzero connection weights: 4879 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| g1AL | M4 | 7 | Yes |
| PLNL | PHCL | 2 | Yes |
| PVDL | ALA | 250 | Yes |
| PVDL | hmc | 400 | Yes |
| PVDR | hmc | 400 | Yes |
| DD6 | PDB | 2 | Yes |
| PDB | DD6 | 2 | Yes |
| ALA | exc_gl | 1 | Yes |
| exc_gl | ALA | 1 | Yes |
| BDUL | PLML | 0 | Yes |
| RMDVR | SMDVR | 8 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected total weight of connections: 23313 (matches)

Expected number of nonzero connection weights: 2883 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for Cook2019MaleReader 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 6 | Yes |
| SMBDL | SDQR | 18 | Yes |
| R7BL | PDC | 34 | Yes |
| DB4 | MDL13 | 4 | Yes |
| RIMR | MDL05 | 15 | Yes |
| CEPDR | RMHL | 6 | Yes |
| URBL | OLLL | 4 | Yes |
| R9BR | R7stR | 2 | Yes |

Expected total weight of connections: 45959 (matches)

Expected number of nonzero connection weights: 5306 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| g1AL | M4 | 7 | Yes |
| CANL | exc_cell | 200 | Yes |
| PVDL | ALA | 250 | Yes |
| URBL | IL2L | 17 | Yes |
| DD1 | MVL08 | 2 | Yes |
| RIVR | FLPL | 0 | Yes |
| DD1 | MVR08 | 2 | Yes |
| R8AL | R8BL | 5 | Yes |
| RIVL | FLPL | 1 | Yes |
| VB6 | VB7 | 5 | Yes |
| VB7 | VB5 | 1 | Yes |
| MDR08 | DD1 | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected total weight of connections: 31702 (matches)

Expected number of nonzero connection weights: 3482 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



## CookEtAl2020

Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).

The connectivity data was released in 2 CSV files in the supplementary information for that paper:

- [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) described as "Complete edge list for pharyngeal reconstruction."

- [cne24932-sup-0005-Supinfo5.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0005-Supinfo5.csv) described as "Inferred gap junction connectivity between end-organs". These connections have been included and some of these tested below also. 

These files were opened in Apple Numbers, and the weights (numbers of connections between pairs of cells, electrical or chemical) were read off, to provide checks listed below. 


### Validation tests for Cook2020DataReader 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 8 | Yes |
| I1R | I2L | 1 | Yes |
| RIPL | pm3VL | 4 | Yes |
| I5 | g1AR | 5 | Yes |
| I5 | g1AL | 8 | Yes |
| I6 | g1P | 2 | Yes |

TODO: add total num nonzero connections

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| e2DR | e3D | 2 | Yes |
| g1AL | M3L | 2 | Yes |
| pm1 | pm2VL | 3 | Yes |
| mc1V | pm3VL | 3 | Yes |
| mc3V | pm7VL | 3 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

TODO: add total num nonzero connections

_Validation PASSED on 2026-06-19 with cect v0.3.2_



## Brittin2021

Data taken from: A multi-scale brain map derived from whole-brain volumetric reconstructions, 
Christopher A. Brittin, Steven J. Cook, David H. Hall, Scott W. Emmons & Netta Cohen, [Nature 591, 105–110, 2021](https://www.nature.com/articles/s41586-021-03284-x).

Supplementary data file 3 ([41586_2021_3284_MOESM5_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03284-x/MediaObjects/41586_2021_3284_MOESM5_ESM.xlsx)) 
containing the M<sup>δ</sup>, C<sup>δ</sup> and G<sup>δ</sup> reference graphs was downloaded and used in the BrittinDataReader.

The M<sup>4</sup> graph is the example used in Connectome Toolbox. Values for the contact area/weights in tab M, with delta = 4 were used for this, and the values below were read from the spreadsheet.




### Validation tests for BrittinDataReader 


#### Contact connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | ADLL | 11319.5 | Yes |
| ADLL | ADAL | 11319.5 | Yes |
| ADLR | ADAR | 11319.5 | Yes |
| ADLR | ADAR | 11319.5 | Yes |
| ADAR | ADLR | 11319.5 | Yes |
| RID | RICL | 10043.5 | Yes |
| RICL | RID | 10043.5 | Yes |
| RICR | RID | 10043.5 | Yes |
| RIAR | SIBVR | 5114.25 | Yes |
| AQR | RIAL | 2010.75 | Yes |
| AQR | RIAR | 2010.75 | Yes |
| RIAR | AQR | 2010.75 | Yes |
| RIAL | AQR | 2010.75 | Yes |

Expected number of nonzero connection weights: 3850 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



## WitvlietEtAl2021

Data on neuronal connectivity at different developmental stages of C. elegans from: Connectomes across development reveal principles of brain maturation
[Witvliet et al. Nature 2021](https://www.nature.com/articles/s41586-021-03778-8). 

While the paper's supplementary information contained connectivity matrices ([here](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03778-8/MediaObjects/41586_2021_3778_MOESM4_ESM.xlsx)), these only contain the chemical connections. 

The 8 spreadsheet files (witvliet_2020_1 L1.xlsx, witvliet_2020_2 L1.xlsx, ..., witvliet_2020_8 adult.xlsx) hosted on [WormWiring](https://wormwiring.org/pages/witvliet.html), also contain electrical connectivity, and are saved to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data), and used for the readers.

The chemical connection weights below were read from the supplementary information spreadsheet, and the electrial connection weights were taken from the WormWiring spreadheet.





### Validation tests for WitvlietDataReader1 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AWAL | AWBL | 2 | Yes |
| AINR | AUAL | 2 | Yes |
| RIAL | RMDVR | 6 | Yes |

Expected number of nonzero connection weights: 775 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASHL | ADAL | 9 | Yes |
| RMDR | SMDVR | 1 | Yes |
| IL1R | IL1VR | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 164 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader2 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASKR | 4 | Yes |
| AUAL | RIBL | 3 | Yes |
| AWBL | AIZL | 2 | Yes |

Expected number of nonzero connection weights: 986 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVJR | RIS | 1 | Yes |
| OLLL | OLLR | 2 | Yes |
| RIH | RIR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 246 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader3 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASKR | 4 | Yes |
| FLPR | FLPL | 3 | Yes |
| RIVL | GLRVR | 2 | Yes |

Expected number of nonzero connection weights: 1012 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| OLLR | RIGR | 1 | Yes |
| OLLL | OLLR | 2 | Yes |
| SMDDL | SMDDR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 186 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader4 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AWCR | AWCL | 5 | Yes |
| RIML | MDR04 | 2 | Yes |
| RIVL | MVR07 | 1 | Yes |

Expected number of nonzero connection weights: 1136 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ALML | AVDR | 2 | Yes |
| AVER | URYVL | 1 | Yes |
| SMDDL | SMDDR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 415 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader5 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASHR | 3 | Yes |
| ALNR | SAAVR | 2 | Yes |
| BAGR | RIBL | 13 | Yes |

Expected number of nonzero connection weights: 1515 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAR | ASHR | 2 | Yes |
| ADLL | CEPshVL | 1 | Yes |
| OLQVL | RIGL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 578 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader6 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASER | ASEL | 1 | Yes |
| ASKR | AIAR | 18 | Yes |
| ALML | CEPVL | 3 | Yes |

Expected number of nonzero connection weights: 1525 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AIZR | AWCL | 2 | Yes |
| BAGR | RIR | 1 | Yes |
| DVA | OLQVL | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 426 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader7 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AQR | BAGR | 4 | Yes |
| ALNR | SAAVR | 11 | Yes |
| CEPDL | OLLL | 7 | Yes |

Expected number of nonzero connection weights: 2202 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | PVQL | 2 | Yes |
| SIAVL | SMDVR | 1 | Yes |
| SAADL | SMBDL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 576 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for WitvlietDataReader8 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASER | AWCR | 9 | Yes |
| ALNL | SAAVL | 10 | Yes |
| ALML | BDUL | 9 | Yes |

Expected number of nonzero connection weights: 2186 (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFL | AIAL | 3 | Yes |
| AFDR | AIZR | 1 | Yes |
| PVT | RIBL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: True

Expected number of nonzero connection weights: 612 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



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


### Validation tests for RipollSanchezShortRangeReader 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I3 | I5 | 3 | Yes |
| URBL | RMDDL | 4 | Yes |
| RIVR | HSNL | 6 | Yes |

Expected number of nonzero connection weights: 31417 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for RipollSanchezMidRangeReader 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| PVR | I3 | 6 | Yes |
| SABVL | VC1 | 1 | Yes |
| RIR | AVKR | 5 | Yes |

Expected number of nonzero connection weights: 40425 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for RipollSanchezLongRangeReader 


#### Peptidergic connections

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

Expected number of nonzero connection weights: 53558 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



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


### Validation tests for Yim2024NonNormDataReader 


#### Contact connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIH | CEPshDL | 7464.984227 | Yes |
| PVNL | ALMR | 97686.4 | Yes |
| URYDR | URADR | 33663.09403 | Yes |

Expected number of nonzero connection weights: 2198 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for Yim2024DataReader 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | AFDR | 0.428024049927915 | Yes |
| SMBDL | RMED | 6.01978135910464 | Yes |
| ASHL | RIPL | 1.20804164634321 | Yes |

Expected number of nonzero connection weights: 2198 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



## WangEtAl2024

This reader combines neurotransmitter expression values from: Wang et al. 2024 (A neurotransmitter atlas of C. elegans males and hermaphrodites, [eLife 13:RP95402](https://doi.org/10.7554/eLife.95402.3)) with basic anatomical connectivity information from Cook et al. 2019, and monoaminergic receptor expression information from Bentley et al 2015.

[Supplementary file 2](https://cdn.elifesciences.org/articles/95402/elife-95402-supp2-v1.xlsx) in that publication contains the expression patterns of neurotransmitter pathway genes in hermaphrodites.
    
This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/elife-95402-supp2-v1.xlsx). 


[Supplementary file 3](https://cdn.elifesciences.org/articles/95402/elife-95402-supp3-v1.xlsx) contains the expression patterns of neurotransmitter pathway genes in male-specific neurons.

This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/elife-95402-supp3-v1.xlsx).

    


### Validation tests for Wang2024HermReader 


#### Acetylcholine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 1 | Yes |
| SMBDL | SDQR | 1 | Yes |
| VC2 | PVT | 1 | Yes |
| DB4 | MDL13 | 1 | Yes |
| M1 | g1P | 1 | Yes |

Expected total weight of connections: 2756 (matches)

Expected number of nonzero connection weights: 2756 (matches)

#### Glutamate connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | MDL05 | 1 | Yes |
| PHBR | AVAR | 1 | Yes |
| URYDL | OLQDL | 1 | Yes |
| PVR | IL1DR | 1 | Yes |

Expected total weight of connections: 1334 (matches)

Expected number of nonzero connection weights: 1334 (matches)

#### Betaine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASIL | AIBL | 1 | Yes |
| NSMR | pm5VR | 1 | Yes |
| RIR | AQR | 1 | Yes |

Expected total weight of connections: 150 (matches)

Expected number of nonzero connection weights: 150 (matches)

#### GABA connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIBL | CEPVL | 1 | Yes |
| VD10 | MVR20 | 1 | Yes |
| SMDDL | SIBDL | 1 | Yes |

Expected total weight of connections: 506 (matches)

Expected number of nonzero connection weights: 506 (matches)

#### Dopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| CEPVL | AIMR | 1 | Yes |
| PDEL | RICR | 1 | Yes |
| ADEL | DD4 | 1 | Yes |

Expected total weight of connections: 1160 (matches)

Expected number of nonzero connection weights: 1160 (matches)

#### Serotonin connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| HSNL | PVQL | 1 | Yes |
| NSML | VD3 | 1 | Yes |
| ADFR | RID | 1 | Yes |

Expected total weight of connections: 492 (matches)

Expected number of nonzero connection weights: 492 (matches)

#### Tyramine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | RMEV | 1 | Yes |
| RIMR | SIADL | 1 | Yes |
| RIML | VD5 | 1 | Yes |

Expected total weight of connections: 224 (matches)

Expected number of nonzero connection weights: 224 (matches)

#### Octopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RICR | ASIL | 1 | Yes |
| RICL | SIAVR | 1 | Yes |
| RICL | PVQL | 1 | Yes |

Expected total weight of connections: 56 (matches)

Expected number of nonzero connection weights: 56 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_




### Validation tests for Wang2024MaleReader 


#### Acetylcholine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 1 | Yes |
| SMBDL | SDQR | 1 | Yes |
| VC2 | PVT | 1 | Yes |
| DB4 | MDL13 | 1 | Yes |
| M1 | g1P | 1 | Yes |

Expected total weight of connections: 3889 (matches)

Expected number of nonzero connection weights: 3889 (matches)

#### Glutamate connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | MDL05 | 1 | Yes |
| CP05 | AVG | 1 | Yes |
| R9AL | HOB | 1 | Yes |

Expected total weight of connections: 1722 (matches)

Expected number of nonzero connection weights: 1722 (matches)

#### Betaine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASIL | AIBL | 1 | Yes |
| NSMR | pm5VR | 1 | Yes |
| RIR | AQR | 1 | Yes |

Expected total weight of connections: 150 (matches)

Expected number of nonzero connection weights: 150 (matches)

#### GABA connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIBL | CEPVL | 1 | Yes |
| VD10 | MVR20 | 1 | Yes |
| SMDDL | SIBDL | 1 | Yes |

Expected total weight of connections: 691 (matches)

Expected number of nonzero connection weights: 691 (matches)

#### Dopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| CEPVL | AIMR | 1 | Yes |
| PDEL | RICR | 1 | Yes |
| ADEL | DD4 | 1 | Yes |

Expected total weight of connections: 1160 (matches)

Expected number of nonzero connection weights: 1160 (matches)

#### Serotonin connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| HSNL | PVQL | 1 | Yes |
| NSML | VD3 | 1 | Yes |
| ADFR | RID | 1 | Yes |

Expected total weight of connections: 492 (matches)

Expected number of nonzero connection weights: 492 (matches)

#### Tyramine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | RMEV | 1 | Yes |
| RIMR | SIADL | 1 | Yes |
| RIML | VD5 | 1 | Yes |

Expected total weight of connections: 224 (matches)

Expected number of nonzero connection weights: 224 (matches)

#### Octopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RICR | ASIL | 1 | Yes |
| RICL | SIAVR | 1 | Yes |
| RICL | PVQL | 1 | Yes |

Expected total weight of connections: 56 (matches)

Expected number of nonzero connection weights: 56 (matches)

_Validation PASSED on 2026-06-19 with cect v0.3.2_



