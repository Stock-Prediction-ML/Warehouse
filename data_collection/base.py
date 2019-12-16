"""Base
This file contains generic functions used in the data collection packages.

    * keys_available - checks if API keys exist for a given API
    * get_api_keys - returns the API keys for a given API

"""
import os
from typing import Dict

def get_api_keys(source: str, path: str) -> Dict[str]:
    """
    Get API keys from file

    Parameters
    ----------
    source : str
        The name of the data source
    path : str, optional
        The path to the key file

    Returns
    -------
    Dict
        A dictionary containing the requested API keys.
        The dict is keyed by the names in key file.
    """

    file_path = str()
    vals = list()

    # expand path if relative
    if path[0] == '~':
        file_path = os.path.expanduser(path)
    elif path[0] == '.':
        file_path = os.path.abspath(path)
    else:
        # assume abs path
        file_path = path

    # read in file assuming a header
    # comma delimited
    with open(file_path, 'r') as in_file:
        in_file.readline().strip().split(',')
        vals = in_file.readline().strip().split(',')
    return vals