import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")


    def test_base(self):
        self.assertEqual(convert(11259375,16),"ABCDEF")
    def test_base12(self):
        self.assertEqual(convert(300,12),"210")

if __name__ == "__main__":
        unittest.main()
