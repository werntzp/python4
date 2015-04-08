"""
composable.py: defines a composable function class.
"""

import types

class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)         
        raise TypeError("Illegal operands for multiplication")
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(
                            self.func.__name__, id(self))
        
    # method to raise x to power x
    def __pow__(self, x):
        "Return the power of incoming integer"
        # test for an integer that is positive 
        if not isinstance(x, int):
            raise TypeError("Must be an integer!")
        if x <= 0:
            raise ValueError("Must be a positive integer.")
        # get internal function (stored in __init__)
        pow = self.func
        # use range to loop through leveraging existing __mul__ method
        for y in range(1, x):
            pow = self.__mul__(pow)
        return pow
        
