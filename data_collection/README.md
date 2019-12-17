# Data Collection

This folder contains the code for scraping data

## API Keys

APIs to data sources are required for data collection.
Keys must be provided in the key file.

* Copy `sample_keys.yaml` 
* Rename to `keys.yaml`
* Add the API keys.

**Do not commit this file.**
This file is git ignored.

## Programming Language Requirements

* **`install.sh`** can be used to install the required dependencies on linux
* `requirements.txt` contains the python requirements

## Code
    ├── abstract_api.py                     # An ABC to unify the API of data collection classes
    ├── base.py                             # A collection of generic functions used in the data collection classes
    ├── tests                               # Unit test files
         ├── test_base.py                   # Tests for base.py
         └──                                # 

## Other Files and Folders

* `stock_symbols/` - This folder contains stock symbols used in the data collection process
