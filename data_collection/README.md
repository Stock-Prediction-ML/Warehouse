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

## Unit Tests

* `run_tests.sh` - Runs the unit tests
* `run_coverage.sh` - Runs the unit tests and produces a coverage report

## Other Files and Folders

* `scraper/` - The data scraping code
* `stock_symbols/` - This folder contains stock symbols used in the data collection process
* `tests/` - Unit tests for `scraper/`
