# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_00(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("2 3.2 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_06(self):
        self.assertEqual(postfix_eval("2 3 <<"),16)
        self.assertEqual(postfix_eval("2 3 >>"),0)

    def test_postfix_eval_07(self):
        try:
            postfix_eval("4 0 /")
            self.fail()
        except ValueError:
            self.assertEqual(0,0)

    def test_postfix_eval_08(self):
        self.assertEqual(postfix_eval('5 1 2 + 4 ** + 3 -'), 83)

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval('7 2 + 6 - 4 - 8 +'), 7)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval('3 2 1 / - 4 5 / 6 - *'), -5.2)

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval('4 3 6 << >>'), 0)
        self.assertAlmostEqual(postfix_eval('6 3 << 4 >>'), 3)

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("6 << 3 >> 4"), "6 3 << 4 >>")
        self.assertEqual(infix_to_postfix("4 >> ( 3 << 6 )"), "4 3 6 << >>")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'), '3 4 2 * 1 5 - 2 3 ** ** / +')

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix('1 + 2 * 3 - 4 / 5 * 6'), '1 2 3 * + 4 5 / 6 * -')

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix('( 1 + 2 << 3 - 4 ) / ( 5 * 6 )'), '1 2 3 << + 4 - 5 6 * /')

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix('( 1 + 2 * 3 - 4 ) >> ( 5 * 6 )'), '1 2 3 * + 4 - 5 6 * >>')

    def test_prefix_to_postfix_1(self):
        self.assertEqual(prefix_to_postfix("* - 3 >> 2 1 - / 4 5 6"), "3 2 1 >> - 4 5 / 6 - *")

    def test_prefix_to_postfix_2(self):
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'), '3 2 1 / - 4 5 / 6 - *')

    def test_prefix_to_postfix_3(self):
        self.assertEqual(prefix_to_postfix('+ + 5 * 6 7 8'), '5 6 7 * + 8 +')

    def test_prefix_to_postfix_4(self):
        self.assertEqual(prefix_to_postfix('+ * 5 6 * 7 8'), '5 6 * 7 8 * +')

if __name__ == "__main__":
    unittest.main()
