import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):
    def test_01(self):
        with self.assertRaises(FileNotFoundError):
            load_concordance_table('testfssdile.txt')
    def test_02(self):
        with self.assertRaises(FileNotFoundError):
            load_stop_table('testfssdile.txt')