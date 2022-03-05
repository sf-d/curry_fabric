import math
import operator
import functools
from itertools import product, repeat
from textwrap import wrap
import numpy as np
np.set_printoptions(suppress=True)
STEPS = 3
class p:
    def __init__ (self, n, intrv):
        self.n = n
        self.start, self.stop = intrv
        self.intrv = intrv
        self.vals = np.linspace(self.start, self.stop, n)



def curry(func):
    def curried(*args):
        if len(args) == func.__code__.co_argcount:
            steps_=set()
            to_pr=[]
            for arg in args:
                v = arg.vals
                to_pr.append(v)
                steps_.add(len(v))
            if len(steps_)==1:
                list_test = np.asarray(list(product(*to_pr)))
                answs=[]
                for i in list_test:
                    p = func(*(i))
                    answs.append(p)
                reshp_list=list_test.reshape((*repeat(list(steps_)[0], func.__code__.co_argcount),func.__code__.co_argcount))
                reshp_answs=np.asarray(answs).reshape((*repeat(list(steps_)[0],func.__code__.co_argcount),1))
                return reshp_list, reshp_answs
            else:
                print(f'steps count not identic: {steps_}')
        else:
            return (lambda *x: curried(*(args + x)))              
    return curried



liv_lot = p(STEPS,(100000,500000))
kit = p(STEPS,(1,10))
liv_dens = p(STEPS,(1,10))
child = p(STEPS,(10,100))
ch_lot_dens = p(STEPS,(1,10))


@curry
def S_child_lot(liv_lot, kit, liv_dens, child, ch_lot_dens): 
    return liv_lot*((kit)/(liv_dens/10000)*child*(ch_lot_dens/10000)) 

list_t, ans = S_child_lot(liv_lot, kit, liv_dens, child, ch_lot_dens)


print (list_t[0,0,0,:,0])

print (list_t[1,1,1,:,1])

