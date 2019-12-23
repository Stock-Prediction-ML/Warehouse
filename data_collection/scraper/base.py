"""Base

"""
import os
import glob
from typing import Dict, List
import yaml

from scraper.abstract_fob import AbstractFob

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

class KeyFob(AbstractFob):

    def __init__(self) -> None:
        """
        Class constructor. 
        """
        super().__init__()

    def set_keys(self, path: str) -> None:
        """
        Get API keys from file

        Parameters
        ----------
        path : str, optional
            The path to the key file
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

        self.path = file_path

        # read the key file (yaml)
        # store keys in instance
        self.keys = self._read_yaml(self.path)

    def get_keyset(self, source: str) -> Dict[str,str]:
        """
        Get a set of api keys from keyfob

        Parameters
        ----------
        source : str
            An available key source

        Returns
        -------
        Dict
            A dictionary containing the requested API keys.
        """
        
        # key error is raised if source is invalid
        return self.keys[source.lower()]

