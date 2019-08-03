import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[0],'')
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_empty_and_single_char(self):
        huffman_encode('blank.txt','blank_sol.txt')
        huffman_encode('testfile.txt','testfilesol.txt')

    def test_file_not_found_encode_0(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode('testfssdile.txt','testfilesol.txt')

    def test_file_not_found_encode_1(self):
        with self.assertRaises(FileNotFoundError):
            cnt_freq('chepis')

    def test_huffman_encode(self):
        huffman_encode('multiline.txt','new_multi.txt')

    def test_01_textfile(self):
        huffman_encode("declaration.txt", "declr_solved.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declr_solved.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_1(self):
        huffman_encode("declaration.txt", "declr_solved.txt")
        huffman_decode("declr_solved.txt", "new_dec.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declr_solved.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_file_not_found_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode('testfssdile.txt','testfilesol.txt')

if __name__ == '__main__':
   unittest.main()
