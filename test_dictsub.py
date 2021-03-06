"""
test_dictsub.py - test the math quiz functions
"""
import unittest
from dictsub import *

class TestDict(unittest.TestCase):

    def test_empty(self):
        # test whether dictionary is empty
        d = MyDict("eagles")
        self.assertEqual(d,{})        
    
    def test_len(self):
        # test checking length
        d = MyDict(6)
        d["fg"] = 3
        d["safety"] = 2
        d["pat"] = 1
        d["2ptconv"] = 2
        # dict should have 4 items
        self.assertEqual(len(d), 4)

    def test_default(self):
        # test returning default value
        d = MyDict(6)
        d["fg"] = 3
        self.assertEqual(d["fg"], 3) # fg worth 3 points
        self.assertEqual(d["td"], 6) # td worth 6 even though we never added it explicitly
        
if __name__ == "__main__":
    unittest.main() 
