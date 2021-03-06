""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

# new function
def groffle_faster(mass, density): 
    total = 0.0 
    # move calculation outside loop 
    masslog = log(mass * density)
    # modify range so no inner calculation needed
    for i in range(1, 10001): 
        total += (masslog/i)

    return total

mass = 2.5 
density = 12.0 

timer = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("time groffle_slow:", timer.timeit(number=1000)) 

timer2 = Timer("total = groffle_faster(mass, density)", 
 "from __main__ import groffle_faster, mass, density") 
print("time groffle_faster:", timer2.timeit(number=1000)) 

slow_val = groffle_slow(mass, density)
faster_val = groffle_faster(mass, density)
if slow_val == faster_val:
    print("Values matched!")
else:
    print("Uh-oh")
    
 
