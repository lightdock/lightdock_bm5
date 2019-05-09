# LightDock Protein-Protein Benchmark 5 Data

## Description

* results: this folder contains for each complex from the BM5 and for each scenario (BLIND, PAIR, TI, TI-REC, TI-25 and TI-50) a file with extension `.list` where for each structure predicted by the protocol its name, interface-RMSD, ligand-RMSD, fraction of native contacts and the final score.

* data: for each complex, the initial PDB structures used, the reference (`*.segid.pdb`) and for each scenario `setup.json` and `lightdock.info` files.


## Reproduction of results

![LightDock-pipeline](media/LightDock-pipeline.png)
