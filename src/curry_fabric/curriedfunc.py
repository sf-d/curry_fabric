from itertools import product

import numpy as np


class p:
    def __init__(self, n, intrv):
        self.n = n
        self.start, self.stop = intrv
        self.intrv = intrv
        self.vals = np.linspace(self.start, self.stop, n)


def curry(func: callable) -> callable:
    """
    :rtype: callable
    """

    def curried(*args):

        if len(args) == func.__code__.co_argcount:
            steps_: set[int] = set()

            steps_.update([len(arg.vals) for arg in args])  # сет получаем через update чтобы облегчить синтаксис

            to_pr = [arg.vals for arg in args]  # упрощаем цикл
            if len(steps_) == 1:
                # векторизируем функцию под numpy аргументы, чтобы избежать длинного цикла подстановки
                vfunc = np.vectorize(func)

                list_test = np.asarray(list(product(*to_pr)))
                answers = vfunc(*list_test.T)

                return np.c_[list_test, answers]
            else:
                print(f'steps count not identical: {steps_}')
        else:
            return lambda *x: curried(*(args + x))

    return curried
