"""
Class-based dict allowing tuple subscripting and sparse data
"""

import array as sys_array

class array:

    def __init__(self, R, C, D):
        """
        Create a three dimensional structure. 
        """
        self._data = {}
        self._rows = R
        self._cols = C
        self._depth = D

    def __getitem__(self, key):
        """
        Returns appropriate item after three dimensional subscript tuple passed in.
        """
        row, col, depth = self._validate_key(key)
        try:
            return self._data[row, col, depth]
        except KeyError:
            return  0

    def __setitem__(self, key, value):
        """
        Sets the appropriate element based on three dimensional subscript tuple.
        """
        row, col, depth = self._validate_key(key)
        self._data[row, col, depth] = value

    def _validate_key(self, key):
        """
        Validate key against the array's shape, returning good tuples. Raises KeyError on problems.
        """
        row, col, depth = key
        if (0 <= row < self._rows and 
            0 <= col < self._cols and 
            0 <= depth < self._depth):
            return key
        raise KeyError("Subscript out of range")
 
