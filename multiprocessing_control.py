"""
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
"""
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
import random

def random_string():
    # generate random string of 1k chars
    chars = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([random.choice(chars) for i in range(1000)])

if __name__ == "__main__":
    WORKERS = 10

    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
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
    print("Control process terminating")

 
