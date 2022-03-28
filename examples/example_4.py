
from curry_fabric.curriedfunc import curry, p
import sys
import numpy as np
import operator
import math
import itertools as it
import plotly.graph_objects as go
from sklearn.decomposition import PCA

np.set_printoptions(precision=3, threshold=sys.maxsize, suppress=True)

STEPS = 5

bi = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
Ab = 4.5
Di = [40, 36, 33, 22, 25, 21, 20, 19, 17]

def prod (x,y):
    res_o = np.reshape(np.asarray(list(it.product(x,y))), (len(bi), len(bi), 2))
    res_one = np.insert(res_o,2, 4.5, axis=2)
    res_two = np.flip(res_one, axis = 0)
    result = []
    for i in range(len(bi)):
        res = list(it.product(res_one[i],res_two[i]))  
        result.extend(res)   
    return np.reshape(np.asarray(result),(729,2,3))

test_ar = prod(bi, Di)

def Si(Ab, bi, Di):
    return Ab*bi*Di

Si_sum = []
for i in test_ar:
    Si_one = Si(*i[0])
    Si_two = Si(*i[1])
    Si_sum.append(Si_one + Si_two)



S_i = np.asarray(Si_sum)
ax_x=(test_ar[:,0,0]).flatten()
ax_y=(test_ar[:,0,1]).flatten()


func_colours = np.repeat('heatmap', len(S_i))

fig = go.Figure(data = [go.Scatter3d(x=ax_x, y=ax_y, z=S_i, mode = 'markers', marker = dict(color = S_i, colorscale='Viridis', opacity=0.8))])
fig.show()
