import timeit
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
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################



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
    neigh_points = points[nearest_neighbor_ids]
    other_points = np.delete(points, nearest_neighbor_ids, 0 )
    return neigh_points, other_points, nearest_neighbor_ids






#remap
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################


def remap_interval(OldValue, OldMin, OldMax, NewMin, NewMax):
    OldRange = OldMax - OldMin
    if OldRange == 0:
        print("none domain length")
    else:

        NewRange = NewMax - NewMin
        NewValue = (OldValue - OldMin) * NewRange / OldRange + NewMin
        return NewValue


def solve_points_domain(points_):
    listx = []
    listy = []
    listz = []
    for i in points_:
        listx.append(i[0])
        listy.append(i[1])
        listz.append(i[2])
    listx.sort()
    listy.sort()
    listz.sort()
    xmax, xmin = listx[0], listx[-1]
    ymax, ymin = listy[0], listy[-1]
    zmax, zmin = listz[0], listz[-1]
    bounds = zip([xmax, xmin], [ymax, ymin], [zmax, zmin])
    return bounds


def solve_normalize(points):
    max_, min_ = solve_points_domain(points.tolist())
    xmx, ymx, zmx = max_
    xmn, ymn, zmn = min_
    ans=[]
    for i in points:
        x_ = remap_interval(i[0], xmn, xmx, 0.0, 1.0)
        y_ = remap_interval(i[1], ymn, ymx, 0.0, 1.0)
        z_ = remap_interval(i[2], zmn, zmx, 0.0, 1.0)
        ans.append( [x_, y_, z_])
    return np.asarray(ans)



#creating charts in plotly
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
goal_arrr = np.array([[L_goal, A_goal, D_sn_goal]])


norm_ar = solve_normalize(np.concatenate((test_ar, goal_arrr), axis=0))
norm_goal = norm_ar[-1]
norm_test = np.delete(norm_ar, -1, 0 )

neigh, other, ind = get_neighbours(norm_test, norm_goal, 10)
norm_g = np.expand_dims(norm_goal, axis=0)


conc_array = np.concatenate((other, neigh, norm_g),axis= 0)






list_x=np.take(conc_array, [0], axis =1)
list_xx = list_x.flatten()

list_y = np.take(conc_array, [1], axis =1)
list_yy = list_y.flatten()

list_z = np.take(conc_array, [2], axis =1)
list_zz = list_z.flatten()


xx=np.array('rgb(255,188,0)')
yy=np.array('rgb(0,119,255)')
zz=np.array('rgb(255,0,0)')
func_colone = np.repeat(xx, len(other))
func_coltwo = np.repeat(yy, len(neigh))
func_colthree = np.repeat(zz, len(norm_g))
text__ = []
for i in range (len(conc_array)):
    conv = str(i)
    text__.append(i)
func_colours=np.concatenate((func_colone,func_coltwo,func_colthree), axis=0)
fig = go.Figure(data = [go.Scatter3d(x=list_xx, y=list_yy, z=list_zz, text = text__ , mode = 'markers', marker = dict(color = func_colours))])
fig.show()

