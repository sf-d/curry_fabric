import math
import operator
import functools
from itertools import product


#def curried(func):
    #def curry(*args, **kwargs):
        #if len(args)+len(kwargs) == func.__code__.co_argcount:
            #ans = func(*args, **kwargs)
            #return ans
        #else:
            #return (lambda *x, **y: curried(*(args + x), **dict(kwargs ,y)))     
            
    #return curry


#list_test = (list(product([0.1, 0.4], repeat = len(args))))

def curried(func):
    def curry(*args):
        if len(args) == func.__code__.co_argcount:
            ans = func(*args)
            return ans
        else:
            return (lambda *x: curried(*(args + x)))     
            
    return curry



@curried
def test(lk, k, p, pd, ld):
    return lk*((k*p*pd)/ld)  


list_test = (list(product([0.1, 0.5, 1] , repeat = 5)))
for i in list_test:
    p = test(*(i))
    print (i,':', p)
      
        

#f__ = test (ld=7, p=3, k=2, pd=6, lk=1)
#print(f'args version: {f_}\nkwargs version: {f__}')    


