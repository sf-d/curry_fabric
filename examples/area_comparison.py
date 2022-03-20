from ast import operator
from itertools import accumulate
from curry_fabric.curriedfunc import curry, p
import sys
from shapely.geometry import MultiPoint, Polygon, LineString
from scipy.spatial import ConvexHull
import numpy as np
from mixpython import geometry as mp
import operator

points =   [[[661.0, 249.0], [750.0, 274.0], [635.0, 276.0]], 
            [[706.0, 355.0], [635.0, 276.0], [750.0, 274.0]], 
            [[706.0, 355.0], [750.0, 274.0], [778.0, 334.0]], 
            [[778.0, 334.0], [672.0, 398.0], [706.0, 355.0]],
            [[778.0, 334.0], [747.0, 511.0], [672.0, 398.0]], 
            [[606.0, 492.0], [672.0, 398.0], [747.0, 511.0]],  
            [[598.0, 428.0], [672.0, 398.0], [606.0, 492.0]]]



# key = list of all points of every minimum polygon 
# нужно разделить предарительно лист всех точек на отдельные полигоны



def joined_list (items):
    f_list = []
    for i in range(len(items)-1, -1, -1):
        n_items = list(accumulate(items[i::-1], operator.add))
        f_list.append(n_items)
    return f_list


def bound_rec (items):
    unshaped = []
    bound_r_area = []
    for bound_r in items:
        for b_r in bound_r:
           ret = mp.minimum_bound_rectangle(np.asarray(b_r))
           bound_area = Polygon(ret.tolist()).area
           unshaped.append(bound_area) 
    last = 0
    for i in range (len(items), 0, -1):
        bound_r_area.append(unshaped[last : last+i])
        last+= i
    return bound_r_area
    

def areas (items):
    areas_trig = []
    for a_t in items:
        ar_trig = Polygon(a_t).area
        areas_trig.append(ar_trig)
    merge_tr_areas = joined_list(areas_trig)
    return merge_tr_areas


def rel_a (a, b):
    relation = []
    ar_relation = []
    for ii, jj in zip(a,b):
        for i,j in zip(ii,jj):
            res = i / j
            relation.append(res)
    last = 0
    for i in range (len(a), 0, -1):
        ar_relation.append(relation[last : last+i])
        last+= i
    return ar_relation


a = joined_list (points)
b = bound_rec(a)
c = areas (points)
d = rel_a(c , b)
print(d)


