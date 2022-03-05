from itertools import product, repeat
import numpy as np
from itertools import product, repeat

import numpy as np

np.set_printoptions(suppress=True)
STEPS = 3


class p:
    def __init__(self, n, intrv):
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
                answs = []
                for i in list_test:
                    p = func(*(i))
                    # возвращвем один массив вместо двух, эта реализация может упростить дальнейшую работу с шейпом, но это не точно
                    answs.append([*i, p])

                # соответственно один решейп
                # reshp_list=list_test.reshape((*repeat(list(steps_)[0], func.__code__.co_argcount),func.__code__.co_argcount))
                reshp_answs = np.asarray(answs).reshape(
                    (*repeat(list(steps_)[0], func.__code__.co_argcount), func.__code__.co_argcount + 1))
                return reshp_answs
            else:
                print(f'steps count not identic: {steps_}')
        else:
            return (lambda *x: curried(*(args + x)))              
    return curried


lk = p(STEPS, (10, 30))
kit = p(STEPS, (1000, 5000))
pp = p(STEPS, (1, 5))
pd = p(STEPS, (0.1, 0.7))
ld = p(STEPS, (100, 300))


@curry
def test(lk, kit, pp, pd, ld):
    return lk * ((kit * pp * pd) / ld)


# один аутпут
ans = test(lk, kit, pp, pd, ld)

# al = list_t.T[:,:,:,1,1,1]
print(ans, ans.T)
