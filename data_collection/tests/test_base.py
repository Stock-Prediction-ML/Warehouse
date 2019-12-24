"""Test_Base
This file contains test for base.py
"""

import unittest
from scraper.base import get_stock_symbols, KeyFob

class TestBase(unittest.TestCase):

    def test_keyfob(self):

        key_fob = KeyFob()
        key_fob.set_keys(path = '../sample_cfg.yaml')
        # test with twitter
        keys = key_fob.get_keyset('twitter')
        # check the number of keys
        key_list = list(keys.keys())
        self.assertEqual(4, len(key_list), msg = 'Check the number of keys returned for Twitter')
        # check for the right keys
        key_list.sort()
        self.assertEqual('APIKey', key_list[0], msg = 'Check for the APIKey key')
        self.assertEqual('APISecretKey', key_list[1], msg = 'Check for the APISecretKey key')
        self.assertEqual('AccessToken', key_list[2], msg = 'Check for the AccessToken key')
        self.assertEqual('AccessTokenSecret', key_list[3], msg = 'Check for the AccessTokenSecret key')
        # check for the right values of the keys
        self.assertEqual('ghfjs', keys['AccessToken'])
        self.assertEqual('nsjugehbwekf', keys['AccessTokenSecret'])
        self.assertEqual('ngwebufoiejdnloaju3712nor', keys['APIKey'])
        self.assertEqual('hi', keys['APISecretKey'])

        # test with alpha vanatage
        keys = key_fob.get_keyset('alpha_vantage')
        # check the number of keys
        key_list = list(keys.keys())
        self.assertEqual(1, len(key_list), msg = 'Check the number of keys returned for Alpha Vantage')
        self.assertEqual('APIKey', key_list[0])
        self.assertIsNone(keys['APIKey'])

    def test_get_stock_symbols(self):

        # basic test
        # just testing that it got something because these files will evolve over time
        nyse_syms = get_stock_symbols('NYSE')
        self.assertGreater(len(nyse_syms), 1)

        # again test that it got something
        # get that AAPL is in it because I expect that AAPL will be there for a while
        nasdaq_syms = get_stock_symbols('nasdaq')
        self.assertGreater(len(nasdaq_syms), 1)
        self.assertTrue('AAPL' in nasdaq_syms)
