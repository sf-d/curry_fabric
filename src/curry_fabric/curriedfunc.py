import math
import operator
import functools
from itertools import product
import numpy as np


def curried(func):
    def curry(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        else:
            return (lambda *x: curried(*(args + x)))              
    return curry




@curried
def test(lk, k, p, pd, ld):
    return lk*((k*p*pd)/ld) 





lk = [10,20,30]

pp = [3,4,5]

list_test = (list(product(pp , repeat = 5)))
for i in list_test:
    p = test(*(i))
    print (i,':', p)
    
      
        

#f__ = test (ld=7, p=3, k=2, pd=6, lk=1)
#print(f'args version: {f_}\nkwargs version: {f__}')    


