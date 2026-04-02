# Validation status of Data Readers

## YimEtAl2024

Data on the dauer connectivity was obtained from the supplementary information of: Yim et al. 2024, Comparative connectomics of dauer reveals developmental plasticity
[Nature Communications, 15:1546](https://www.nature.com/articles/s41467-024-45943-3).

Supplementary Data 3 links to file [41467_2024_45943_MOESM6_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM6_ESM.xlsx).

This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM6_ESM.xlsx).

### Normalised data

The spreadsheet contained a sheet named "Dauer_normalized", from where the vales were read. 

### Validation tests for Yim2024DataReader

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | AFDR | 0.428024049927915 | Yes |
| SMBDL | RMED | 6.01978135910464 | Yes |
| ASHL | RIPL | 1.20804164634321 | Yes |


## CookEtAl2020

Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).




### Validation tests for Cook2020DataReader

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 3 | Yes |


