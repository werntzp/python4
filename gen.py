"""
gen.py - time difference in using list comprehension and list() function
"""
from timeit import Timer

# list of a million random numbers
timer1 = Timer("lst = [random() for i in range(1000000)]","from random import random")
print("list comprehension time:", timer1.timeit(5))

# now do it with list()
timer2 = Timer("lst = list(random() for i in range(1000000))","from random import random")
print("list() time:", timer2.timeit(5))
 
