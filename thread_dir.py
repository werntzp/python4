"""
thread_dir.py - determines whether changing the current directory using os.chdir in one thread changes the current directory for:
1. a thread that already existed before the call to os.chdir.
2. a thread that is created after the call to os.chdir.
"""

import threading
import time
import os

def getcwd():
    # return current folder
    return os.getcwd()

# change the directory
def thread_changedirectory():
    os.chdir(r"v:\workspace\python4_homework10")
    print("thread_changedirectory set current directory to v:\workspace\python4_homework10")
    
# existing threat
def thread_before():
    print("At enter, thread_before current directory is:", getcwd())
    # just idle to give next thread enough time to call
    time.sleep(3)
    print("At exit, thread_before current directory is:", getcwd())

# new thread
def thread_after():
    # just idle to give previous thread time to complete 
    time.sleep(3)
    print("At exit, thread_after current directory is:", getcwd())

# step 1, call prior to changing directory
print("Setting current directory to c:\program files\eclipse")
os.chdir(r"C:\Program Files\Ellipse")
t1 = threading.Thread(target=thread_before)
t1.start()

# step 2, now, call thread in which we change directory
t2 = threading.Thread(target=thread_changedirectory)
t2.start()

# step 3, call final thread to see if it sees changed directory
t3 = threading.Thread(target=thread_after)
t3.start()

# Conclusions:
# 1. Yes, if a thread is going on while the dir is changed, it will see that as current directory
# 2. Yes, any thread called after os.chdir will also see that updated folder

 
