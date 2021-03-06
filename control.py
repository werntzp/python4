"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
import random
import time

def random_string():
    # generate random string of 1k chars
    chars = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([random.choice(chars) for i in range(1000)])

WORKERS = 10

# get start time
start = time.time() 

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
# switch to use the random string
for work in enumerate(random_string()): 
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()

# stop timer and print results 
stop = time.time() 
print("It took {0} seconds to run".format(stop-start))

print("Control thread terminating")

 
