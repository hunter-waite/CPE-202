import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
    def test_perm_gen_lex_2(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
    def test_perm_gen_lex_3(self):
        self.assertEqual(perm_lex.perm_gen_lex('cat'),['cat','cta','act','atc','tca','tac'])
    def test_perm_gen_lex_4(self):
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
if __name__ == "__main__":
        unittest.main()
