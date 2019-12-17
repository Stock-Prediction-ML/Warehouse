"""Base
This file contains generic functions used in the data collection packages.

    * keys_available - checks if API keys exist for a given API
    * get_api_keys - returns the API keys for a given API

"""
import os
import glob
from typing import Dict, List
import yaml

def get_api_keys(source: str, path: str = './keys.yaml') -> Dict[str,str]:
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
        keys = yaml.load(in_file, Loader = yaml.FullLoader)[source]
    return keys

def get_stock_symbols(market: str) -> List[str]:
    """
    Read stock symbols from internal file

    Parameters
    ----------
    market: str
        The stock market (NASDAQ | NYSE)
    
    Returns
    -------
    List
        A list of symbols for the given market
    """

    sym = str()
    syms = list()
    sym_files = list()

    # glob the sym files and get all the markets
    sym_files = glob.glob('./stock_symbols/sym_*.txt')
    for sym in sym_files:
        syms.append(sym.strip().replace('.txt','').split('_')[2])
    if market.upper() not in syms:
        print(syms)
        raise Exception

    # read out symbols for given market
    # market file name should be sym_<MARKET_NAME> located at ./stock_symbols/
    symbols = list()
    with open('./stock_symbols/sym_' + market.upper() + '.txt') as market_file:
        for line in market_file:
            symbols.append(line.strip())
    return symbols
