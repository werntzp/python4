""""
test_decorator.py - test that decorate passes in new arg
"""
import unittest
from decorator import *

class TestAddArg(unittest.TestCase):

    def test_addarg(self):
        # call addarg with a 1
        @addarg(1)
        def prargs(*args):
            return args
        # test that 1 will shot up as first parameter
        self.assertEqual(str(prargs(2, 3)), "(1, 2, 3)", "Expecting '(1,2,3)'")
        self.assertEqual(str(prargs("child")), "(1, 'child')", "Expecting '(1, 'child')'")

if __name__ == "__main__":
    unittest.main()
 
