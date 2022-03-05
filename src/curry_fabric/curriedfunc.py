from itertools import product, repeat
import numpy as np

class p:
    def __init__(self, n, intrv):
        self.n = n
        self.start, self.stop = intrv
        self.intrv = intrv
        self.vals = np.linspace(self.start, self.stop, n)

def curry(func):
    def curried(*args):

        if len(args) == func.__code__.co_argcount:
            steps_ = set()
            to_pr = []
            for arg in args:
                v = arg.vals
                to_pr.append(v)
                steps_.add(len(v))
            if len(steps_) == 1:
                list_test = np.asarray(list(product(*to_pr)))
                answers = []
                for i in list_test:
                    ans = func(*(i))

                    answers.append([*i, ans])

                # reshp_list=list_test.reshape((*repeat(list(steps_)[0], func.__code__.co_argcount),
                # func.__code__.co_argcount))
                reshape_answer = np.asarray(answers).reshape(
                    (*repeat(list(steps_)[0], func.__code__.co_argcount), func.__code__.co_argcount + 1))
                return reshape_answer
            else:
                print(f'steps count not identical: {steps_}')
        else:
            return lambda *x: curried(*(args + x))

    return curried
