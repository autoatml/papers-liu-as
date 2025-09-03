# Research data for "Medium-range structural order in amorphous arsenic"

This repository contains raw data, plotting scripts, and workflow configurations to accompany the manuscript:

<div align="center">

> **[Medium-range structural order in amorphous arsenic](https://arxiv.org/abs/2509.02484)** <br>
> _Yuanbin Liu, Yuxing Zhou, Richard Ademuwagun, Luc Walterbos, <br>
> Janine George, Stephen R. Elliott, Volker L. Deringer_

</div>

## Contents

1. `Workflows/`: Configuration files and scripts for running automated potential-generation workflows.  
2. `Figures/`: Raw data and Jupyter notebooks used to generate the figures presented in the paper.  
3. `Potentials/`: Resources related to the training of machine-learned interatomic potentials, including:
   - `dataset/`: Reference DFT data used for training, validation, and testing.  
   - `models/`: Trained potential models.  
   - `training_script/`: Scripts and configurations for reproducing the training workflow.  

**Note**: Additional data on chemical bonding will be made available via [Zenodo]() upon acceptance. 

## Installation

To install the required packages for reproducing workflows and figures, first create a clean Python environment (e.g., using `conda` or `venv`), then run:

```bash
pip install -r requirements.txt
```

## License

The contents of the `workflows` folder are licensed under the MIT License ([LICENSE_CODE](./LICENSE_CODE)).
