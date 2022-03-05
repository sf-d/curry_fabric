from curry_fabric.curriedfunc import curry, p

import numpy as np
from sklearn.decomposition import PCA

np.set_printoptions(precision=3, suppress=True)

STEPS = 3

lk = p(STEPS, (10, 30))
kit = p(STEPS, (1000, 5000))
pp = p(STEPS, (1, 5))
pd = p(STEPS, (0.1, 0.7))
ld = p(STEPS, (100, 300))


@curry
def test(lk, kit, pp, pd, ld):
    return lk * ((kit * pp * pd) / ld)


def test_(lk, kit, pp, pd, ld):
    return lk * ((kit * pp * pd) / ld)

print(test_( 30. ,   5000. ,     5. ,      0.7 ,   300. ))