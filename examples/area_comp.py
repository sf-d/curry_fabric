from tkinter import E
from iteration_utilities import deepflatten
from curry_fabric.curriedfunc import curry, p
import sys
from shapely.geometry import MultiPoint, Polygon, LineString
from scipy.spatial import ConvexHull
import numpy as np
from mixpython import geometry as mp
from functools import reduce




points =   [[[661.0, 249.0], [750.0, 274.0], [635.0, 276.0]], 
            [[706.0, 355.0], [635.0, 276.0], [750.0, 274.0]], 
            [[706.0, 355.0], [750.0, 274.0], [778.0, 334.0]], 
            [[778.0, 334.0], [672.0, 398.0], [706.0, 355.0]],
            [[778.0, 334.0], [747.0, 511.0], [672.0, 398.0]], 
            [[606.0, 492.0], [672.0, 398.0], [747.0, 511.0]],  
            [[598.0, 428.0], [672.0, 398.0], [606.0, 492.0]]]
              

 

    
def analyze_func(points):
    
    #get the sliced list
    l = len(points)
    res_=[]
    for j in range(l+1):
        res = [[points]]
        for idx in range(j-1):
            res = [[*strt, end[:y], end[y:]] for *strt, end in res
                for y in range(1, len(end) - j + idx + 2)]
        res_.append(res)
    del res_[0] 
    #Вычисление баундинг ректангла
    def bound_rec():
        rel_area = []
        for element in res_:
            #первый элемент списка - смердженный эррэй
            if res_.index(element) == 0:
                flat_el = list(deepflatten(element, depth=3))
                #баундинг ректангл и его площадь
                rect = mp.minimum_bound_rectangle(np.asarray(flat_el))
                bound_area = Polygon(rect.tolist()).area
                tr_area = sum ([Polygon(tr_a).area for tr_a in points ])
                rel = tr_area / bound_area
                rel_area.append(rel)
            else:
                for el in element:
                    area_ = []
                    for e in el:
                        flat_el = list(deepflatten(e, depth=1))
                        rect = mp.minimum_bound_rectangle(np.asarray(flat_el))
                        bound_area = Polygon(rect.tolist()).area
                        tr_area = sum ([Polygon(tr_a).area for tr_a in e ])
                        rel = tr_area / bound_area
                        area_.append(rel)
                    avg = sum(area_) / len(area_) 
                    rel_area.append(avg)
        av_relation = rel_area.index(max(rel_area[1:]))
    #    print (av_relation)
   #     print(rel_area)
        flat_res = list(deepflatten(res_, depth=1))
        return flat_res[av_relation]
    return bound_rec()
                      
v = analyze_func(points)
print(v)