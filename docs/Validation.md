# Validation status of Data Readers

## WhiteEtAl1986

Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

The primary source of this data is https://www.wormatlas.org/neuronalwiring.html, and the []

TODO...

### Validation tests for White_A


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_A_expected_data.yaml**



### Validation tests for White_L4


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_L4_expected_data.yaml**



### Validation tests for White_whole


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//White_whole_expected_data.yaml**



## VarshneyEtAl2011

TODO...

### Validation tests for VarshneyDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//VarshneyDataReader_expected_data.yaml**



## BentleyEtAl2016

TODO...



### Validation tests for WormNeuroAtlasMAReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasMAReader_expected_data.yaml**



### Validation tests for WormNeuroAtlasPepReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasPepReader_expected_data.yaml**



## CookEtAl2019

TODO...

### Validation tests for Cook2019HermDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019HermDataReader_expected_data.yaml**



### Validation tests for Cook2019MaleDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Cook2019MaleDataReader_expected_data.yaml**



## CookEtAl2020

Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).

TODO...

### Validation tests for Cook2020DataReader

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 3 | Yes |
| I1R | I2L | 1 | Yes |

_Validation PASSED on 2026-04-07 with cect v0.3.1_



## BrittinEtAl2021

TODO...

### Validation tests for BrittinDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//BrittinDataReader_expected_data.yaml**



## WitvlietEtAl2021

TODO...

### Validation tests for WitvlietDataReader1


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader1_expected_data.yaml**



### Validation tests for WitvlietDataReader2


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader2_expected_data.yaml**



### Validation tests for WitvlietDataReader3


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader3_expected_data.yaml**



### Validation tests for WitvlietDataReader4


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader4_expected_data.yaml**



### Validation tests for WitvlietDataReader5


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader5_expected_data.yaml**



### Validation tests for WitvlietDataReader6


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader6_expected_data.yaml**



### Validation tests for WitvlietDataReader7


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader7_expected_data.yaml**



### Validation tests for WitvlietDataReader8


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WitvlietDataReader8_expected_data.yaml**



## RandiEtAl2023

TODO...

### Validation tests for WormNeuroAtlasFuncReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//WormNeuroAtlasFuncReader_expected_data.yaml**



## RipollSanchezEtAl2023



### Validation tests for RipollSanchezShortRangeReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//RipollSanchezShortRangeReader_expected_data.yaml**



### Validation tests for RipollSanchezMedRangeReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//RipollSanchezMedRangeReader_expected_data.yaml**



### Validation tests for RipollSanchezLongRangeReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//RipollSanchezLongRangeReader_expected_data.yaml**



## YimEtAl2024

Data on the dauer connectivity was obtained from the supplementary information of: Yim et al. 2024, Comparative connectomics of dauer reveals developmental plasticity
[Nature Communications, 15:1546](https://www.nature.com/articles/s41467-024-45943-3).

Supplementary Data 3 links to file [41467_2024_45943_MOESM6_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM6_ESM.xlsx).

This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM6_ESM.xlsx).

### Normalised data

The spreadsheet contained a sheet named "Dauer_normalized", from where the values were read and added to the connection test yaml file. 

### Validation tests for Yim2024DataReader

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | AFDR | 0.428024049927915 | Yes |
| SMBDL | RMED | 6.01978135910464 | Yes |
| ASHL | RIPL | 1.20804164634321 | Yes |

_Validation PASSED on 2026-04-07 with cect v0.3.1_



### Validation tests for Yim2024NonNormDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Yim2024NonNormDataReader_expected_data.yaml**



## WangEtAl2025

TODO...

### Validation tests for Wang2024HermDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024HermDataReader_expected_data.yaml**



### Validation tests for Wang2024MaleDataReader


**TODO: add expected data file: /Users/padraig/git/ConnectomeToolbox/cect/validation//Wang2024MaleDataReader_expected_data.yaml**



