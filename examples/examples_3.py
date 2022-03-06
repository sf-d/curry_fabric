from curry_fabric.curriedfunc import curry, p
import sys
import numpy as np
import operator
import plotly.express as px
import plotly.graph_objects as go
from scipy.special import expit




np.set_printoptions(precision=3, threshold=sys.maxsize, suppress=True)

STEPS = 15

L = p(STEPS, (5000000, 50000000))
A = p(STEPS, (1000000, 5000000))


@curry
def D_sn(L, A):
    return L / A

test_ar = D_sn(L, A)


#Целевые показатели
D_sn_goal = 15
A_goal = 2600000
L_goal = 39000000
goal_ar = np.array([L_goal, A_goal, D_sn_goal])


 
def get_neighbours(points, goal, k):
    distances = []
    neighbors = []
    for p in points:
        dist = np.linalg.norm(p - goal)
        distances.append((p, dist))
    distances.sort(key=operator.itemgetter(1))
    for x in range(k):
        neighbors.append(distances[x][0])
        n = np.asanyarray(neighbors)
    return n
 
neigh = get_neighbours(test_ar, goal_ar, 10)
print (goal_ar)
print(neigh)




list_a=np.take(test_ar, [0], axis =1)
list_aa = list_a.flatten()

list_b = np.take(test_ar, [1], axis =1)
list_bb = list_b.flatten()

list_c = np.take(test_ar, [2], axis =1)
list_cc = list_c.flatten()



fig = px.scatter_3d(x=list_aa, y=list_bb, z=list_cc, text=range(len(list_bb)))
fig.show()
