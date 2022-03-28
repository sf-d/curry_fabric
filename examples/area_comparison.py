from ast import operator
from itertools import accumulate, product, combinations, islice
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


## зачистить функции



#def joined_list (items):
    #f_list = []
    #for i in range(len(items)-1, -1, -1):
       # n_items = list(accumulate(items[i::-1], operator.add))
       # f_list.append(n_items)
   # return f_list

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


sorted_list = joined_list (points)
b_rect = bound_rec(sorted_list)
tr_areas = areas (points)
relations_of_areas = rel_a(tr_areas, b_rect)

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################



def add_zeroes (arr):
    new_arr =[]
    for i in arr:
        if len(i) < len(arr):
            i.extend([0]*(len(arr)-len(i)))
            new_arr.append(i)
        else:
            new_arr.append(i)
    return new_arr

null_rel_ar = add_zeroes(relations_of_areas)   
            
def diagonalOrder(matrix, ROW,COL):
    d_order = []
 
    for line in range(1, (ROW + COL)):
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)
        d_o =[]
        for j in range(0, count):
            d_o.append(matrix[min(ROW, line) - j - 1][start_col + j])
        d_order.append(d_o)
        
    return d_order[len(d_order)//2::-1]
 
          
            
diag_order = diagonalOrder(null_rel_ar, len(relations_of_areas), len(relations_of_areas))








######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

'''test_sample'''
test_sample  = []
for i in diag_order:
    t_s = []
    for j in i:
        a = diag_order.index(i)
        b = i.index(j)
        j = str(a)+'_'+str(b)
        t_s.append(j)
    test_sample.append(t_s)
 


