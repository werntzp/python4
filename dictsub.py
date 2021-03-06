"""
dictsub.py - subclass a standard dict class
"""

class MyDict(dict):

    def __init__(self, val):
        """
        Init method takes additional default value
        """
        # call dict's init method
        dict.__init__(self) 
        # store the default value
        self._val = val
        
    def __getitem__(self, key):
        """
        Get item returns dict item, unless there is a KeyError in which case it returns default value sent in on creation
        """
        try: 
            return dict.__getitem__(self, key) # key exists
        except KeyError:
            return self._val # pass back out value stored in init
         
