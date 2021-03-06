""""
sstr.py - subclass of str implementing "<<" and ">>"
"""

class sstr(str):
        
    # init method calls super's init, and stores incoming value
    def __init__(self, s):
        super().__init__() 
        self._str= s 
        
    # left shift for string
    def __lshift__(self, n): 
        # make sure n is int
        if not isinstance(n, int):
            raise ValueError("Shift must be an int")
        # if 0, just return the string
        if n == 0:
            return self._str
        # if greater than string, punt
        if n > len(self._str):
            raise ValueError("Cannot shift more than length of string")
        # otherwise, slice and return
        return sstr(self._str[n:] + self._str[:n])

    # right shift for string
    def __rshift__(self, n): 
        # make sure n is int
        if not isinstance(n, int):
            raise ValueError("Shift must be an int")
        # if 0, just return the string
        if n == 0:
            return self._str
        # if greater than string, punt
        if n > len(self._str):
            raise ValueError("Cannot shift more than length of string")
        # otherwise, slice and return
        return sstr(self._str[len(self._str) - n:] + self._str[:-n])
 
