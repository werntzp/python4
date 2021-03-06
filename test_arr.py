"""
Three-dimensional array tests
"""

import unittest
import arr

class TestArray(unittest.TestCase):

    def test_zeros(self):
        """
        All array elements should be zero
        """
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0, "Expecting a zero!")

    def test_identity(self):
        """
        Identity matrix should be one
        """
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i==j==k, "Expecting a one!")
    
    def _index(self, a, r, c, d):
        """
        Return back index based on tuple
        """
        return a[r, c, d]
    
    def test_key_validity(self):
        """
        Validate key for row, column and depth
        """
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)

if __name__ == "__main__":
    unittest.main() 
