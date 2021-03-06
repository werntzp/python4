""""
test_sstr.py - test the sstr subclass
"""
import unittest
from sstr import *

class TestSstr(unittest.TestCase):

    def test_shift_left(self):
        s = sstr("abcde")
        self.assertEqual(s << 0, "abcde")
        self.assertEqual(s << 2, "cdeab")
        self.assertEqual(s >> 5, "abcde")
    
    def test_shift_right(self):
        s = sstr("abcde")
        self.assertEqual(s >> 0, "abcde")
        self.assertEqual(s >> 2, "deabc")

    def test_shift_multiple(self):
        s = sstr("abcde")
        self.assertTrue((s >> 5) << 5 ==  "abcde")
        
if __name__ == "__main__":
    unittest.main() 
