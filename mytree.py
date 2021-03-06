"""
Enhanced tree class with value storage and find ability
"""
class Tree:
    
    def __init__(self, key, value = None):
        """
        Create new tree object
        """
        self._key = key
        self._left = self._right = None
        self._value = value
    
    def insert(self, key, value = None):
        """
        Insert new element, raise error if duplicate
        """
        if key < self._key:
            if self._left:
                self._left.insert(key, value)
            else:
                self._left = Tree(key, value)
        elif key > self._key:
            if self._right:
                self._right.insert(key, value)
            else:
                self._right = Tree(key, value)
        else:
            # 4/7 - could eithe raise error, or just replace that key value
            self._value = value
            # raise ValueError("Attempt to insert duplicate")
    
    def walk(self):
        """
        Generate keys from tree
        """
        if self._left:
            for n in self._left.walk():
                yield n
            yield self._key
            if self._right:
                for n in self._right.walk():
                    yield n

    def find(self, key):
        """
        Return value associated with key, otherwise raises an error
        """
        if key < self._key and self._left:
            return self._left.find(key)
        elif key > self._key and self._right:
            return self._right.find(key)
        elif key == self._key:
            return self._value
        else:
            raise KeyError("Key does not exist!")

if __name__ == "__main__":
    v = 0
    t = Tree("D", v)
    for k in "BJQKFAC":
        v += 1
        t.insert(k, v)
    print("Tree walk:", list(t.walk()))    
    print("Initial value of key Q:", t.find("Q"))
    
    # 4/7 - change value of Q 
    t.insert("Q", 7)
    print("Updated value of key Q:", t.find("Q"))
    
    # 4/7 - try/except catching the KeyError
    try:
        print("Value of key Z:", t.find("Z"))
    except:
        print("KeyError correctly raised when trying to find key Z")
    
                     
