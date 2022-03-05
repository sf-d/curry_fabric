from curry_fabric.curriedfunc import curry, p

import numpy as np
from sklearn.decomposition import PCA

STEPS = 3

lk = p(STEPS, (10, 30))
kit = p(STEPS, (1000, 5000))
pp = p(STEPS, (1, 5))
pd = p(STEPS, (0.1, 0.7))
ld = p(STEPS, (100, 300))


@curry
def test(lk, kit, pp, pd, ld):
    return lk * ((kit * pp * pd) / ld)

