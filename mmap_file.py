"""
mmap_file - Write a program that creates a ten megabyte data file in two different ways and times each method.
"""

from timeit import Timer
import mmap
import os

# method #1 - use mmap
def mmap_file(n, s, c):
    
    with open(n, "w+b") as f:
        mapf = mmap.mmap(f.fileno(), s, access=mmap.ACCESS_WRITE)
        i = 0
        # don't exceed 10MB file size
        while i+c < s:
            j = i + c
            mapf[i:j] = c * b"0"
            i = j
        mapf.close()

# method 2 - use write method
def write_file(n, s, c):
    
    with open(n, "w+b") as f:
        i = 0
        # don't exceed 10MB file size
        while i < s:
            f.write(c * b"0")
            i += c

if __name__ == '__main__':
    
    # list of chunks to use
    CHUNKS = [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024*1024, 2048*2048, 4098*2048]
    FILENAME = "my_big_file"
    FILESIZE = 10485760
    
    # create file with mmap
    print("mmap chunk timers:")
    for c in CHUNKS:  
        mmap_timer = Timer("mmap_file(FILENAME, FILESIZE, c)", "from __main__ import mmap_file, FILENAME, FILESIZE, c")         
        print("chunk size {0} took {1} seconds.".format(c, mmap_timer.timeit(1)))

    print("")

    # delete the file
    try: 
        os.remove(FILENAME)
    except:
        pass
    
    # do it again but with write() method
    print("write() chunk timers:")
    for c in CHUNKS:
        write_timer = Timer("write_file(FILENAME, FILESIZE, c)", "from __main__ import write_file, FILENAME, FILESIZE, c")         
        print("chunk size {0} took {1} seconds.".format(c, write_timer.timeit(1)))

    # delete the file
    try: 
        os.remove(FILENAME)
    except:
        pass

    print("completed")
     
