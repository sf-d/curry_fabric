import math
import operator
import functools



def curried(func):
    def curry(*args, **kwargs):
        if len(args)+len(kwargs) == func.__code__.co_argcount:
            ans = func(*args, **kwargs)
            return ans
        else:
            return (lambda *x, **y: curried(*(args + x), **dict(kwargs ,y)))
    return curry

@curried
def test(lk, k, p, pd, ld):
    return lk*((k*p*pd)/ld)  

f_ = test (1, 2, 3, 6, 7)
f__ = test (ld=7, p=3, k=2, pd=6, lk=1)
print(f'args version: {f_}\nkwargs version: {f__}')    


