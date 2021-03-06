"""
func_inspector.py - Walk through a module and print out function declarations
"""

import inspect
import mymod 

# create list of all the functions in the module
for f in inspect.getmembers(mymod, inspect.isfunction):
    # break out name and object
    name, obj = f
    # pull out the args for each 
    args = inspect.formatargspec(*inspect.getfullargspec(obj))
    # print out so looks like from .py file
    print("def {0}{1}".format(name, args))
     
