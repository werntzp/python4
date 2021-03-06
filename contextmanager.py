"""
contextmanager.py - Write a context manager class that suppresses any ValueError exceptions that occur in the controlled suite, but allows any other exception to be raised in the surrounding context.
"""

from contextlib import contextmanager

@contextmanager
def ctx_man(raising=False):
    try:
        # doesn't do much
        yield 
    # suppress a value error
    except ValueError: 
        print("ValueError suppressed")
        pass    
    # let any other error get raised    
    except Exception as e:
        print("Exception", e, "raised")
        if raising:
            print("Re-raising exception")
            raise

if __name__ == "__main__":
    
    # simple suppression 
    with ctx_man():
        raise ValueError
    
    # more complicated but still suppressed
    with ctx_man():
        i = int("eagles")
    
    # let this error get raised
    with ctx_man() as cm:
        i = 1 / 0


 
