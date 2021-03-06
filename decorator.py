""""
decorator.py - decorator that takes an arg and adds it as first arg to anything decorated
"""

def addarg(a):
    """
    Returns decorator which includes adding an argument
    """
    def my_decorator(f):
        # nested decorator 
        def wrapper(*args, **kwargs):
            # this is where we stick the incoming arg in as first argument to func 
            return f(a, *args, **kwargs)
        return wrapper
    return my_decorator
 
