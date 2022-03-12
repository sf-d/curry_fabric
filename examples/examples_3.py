from curry_fabric.curriedfunc import curry, p
import sys
import numpy as np
import operator
import math
import plotly.graph_objects as go




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
    for p in points:
        dist = math.sqrt((p[0] - goal[0])**2 + (p[1] - goal[1])**2 + (p[2] - goal[2])**2)
        distances.append(dist)
    d = sorted(distances)    
    distances_ = np.asarray(distances)
    nearest_neighbor_ids = distances_.argsort()[:k]
    return points[nearest_neighbor_ids]

neigh = get_neighbours(test_ar, goal_ar.T, 10)
print (neigh)


goal_arrr = np.array([[L_goal, A_goal, D_sn_goal]])
conc_array = np.concatenate((test_ar, goal_arrr, neigh),axis= 0)
print (len(conc_array))
print (len(test_ar))
#creating charts in plotly



list_a=np.take(conc_array, [1], axis =1)
list_aa = list_a.flatten()

list_b = np.take(conc_array, [2], axis =1)
list_bb = list_b.flatten()

list_c = np.take(conc_array, [0], axis =1)
list_cc = list_c.flatten()


a=np.array('rgb(255,188,0)')
b=np.array('rgb(0,119,255)')
c=np.array('rgb(255,0,0)')
func_colone = np.repeat(a, len(test_ar))
func_coltwo = np.repeat(b, len(neigh))
func_colthree = np.repeat(c, len(goal_arrr))
text__ = []
for i in range (len(test_ar+1)):
    conv = str(i)
    text__.append(i)
func_colours=np.concatenate((func_colone,func_coltwo,func_colthree), axis=0)
fig = go.Figure(data = [go.Scatter3d(x=list_aa, y=list_bb, z=list_cc, text = text__ , mode = 'markers', marker = dict(color = func_colours))])
fig.show()
