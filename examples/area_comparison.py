from curry_fabric.curriedfunc import curry, p
import sys
from shapely.geometry import MultiPoint, Polygon, LineString
import plotly.graph_objects as go
from scipy.spatial import ConvexHull
import numpy as np
from mixpython import geometry as mp

points =   [[[661.0, 249.0], [750.0, 274.0], [635.0, 276.0]], 
            [[706.0, 355.0], [635.0, 276.0], [750.0, 274.0]], 
            [[706.0, 355.0], [750.0, 274.0], [778.0, 334.0]], 
            [[778.0, 334.0], [672.0, 398.0], [706.0, 355.0]], 
            [[606.0, 492.0], [672.0, 398.0], [747.0, 511.0]], 
            [[598.0, 428.0], [672.0, 398.0], [606.0, 492.0]], 
            [[778.0, 334.0], [747.0, 511.0], [672.0, 398.0]]]



# key = list of all points of every minimum polygon 
# нужно разделить предарительно лист всех точек на отдельные полигоны



# класс предполанает вгоняние точек по 3 и построения на основе них дерева с вычислением всех баунд рект
# далее функция которая записывает классы
# snachala slivat'?

def split_array (obj):
    array = []
    for i in range(len(obj)):
        if i <= (len(obj) - 3):
            ar = (*obj[i], *obj[i+1], *obj[i+2])
            array.append(ar)
        elif i == len(obj)-2:
            ar_= (*obj[-2], *obj[-1])
            array.append(ar_)
        else:
            ar__ = obj[-1]
            array.append( ar__)
    return array

splitted_array = split_array(points)

# нужно точно такую же херню применить к последовательности эррэей, т.е дописать разветвоение (возможно этот цикл должен быть чуть сложнее и генерить новые списки по ходу) 
#те паттерн развивается в зависимости от того какой минимальный ректангл был выбран - нулевой, первый или второй
#возможно первое значение независимо от точек
# v zelom mozhno dopisat dlya kazhdogo 1+2 i 1+2+3 i t d otdelniy pattern

########### PROVERIT' VICHISLENIYA V FORMULE!!!!

def bound_rect (points_ar):
    p_areas = []
    for p in points_ar:
    
        if points_ar.index(p) <= (len(points_ar) - 3):
            b_rect_one, b_rect_oneone = Polygon(mp.minimum_bound_rectangle(np.asarray(p[0:3]))).area, Polygon(mp.minimum_bound_rectangle(np.asarray(p[3:6]))).area
            b_rect_two = Polygon(mp.minimum_bound_rectangle(np.asarray(p[0:6]))).area + Polygon(mp.minimum_bound_rectangle(np.asarray(p[6:]))).area
            b_rect_three = Polygon(mp.minimum_bound_rectangle(np.asarray(p))).area
            c_one = (b_rect_one / (Polygon(p[0:3]).area) + (b_rect_oneone / Polygon(p[3:6]).area))
            c_two = b_rect_two / (Polygon(p[0:3]).area + Polygon(p[3:6]).area + Polygon(p[6:]).area)
            c_three = b_rect_three / (Polygon(p[0:3]).area + Polygon(p[3:6]).area + Polygon(p[6:]).area)
            p_areas.append([c_one, c_two, c_three])
        elif points_ar.index(p) == len(points_ar)-2:
            b_rect__one = Polygon(mp.minimum_bound_rectangle(np.asarray(p[0:3]))).area + Polygon(mp.minimum_bound_rectangle(np.asarray(p[3:]))).area
            b_rect__two = Polygon(mp.minimum_bound_rectangle(np.asarray(p))).area
            c__one = b_rect__one / (Polygon(p[0:3]).area + Polygon(p[3:6]).area)
            c__two = b_rect__two / (Polygon(p[0:3]).area + Polygon(p[3:6]).area)
            p_areas.append([c__one, c__two])
        else:
            b_rect___one = Polygon(mp.minimum_bound_rectangle(np.asarray(p))).area
            c___one = b_rect___one / Polygon(p).area
            p_areas.append(c___one)            
    return p_areas


rectangles = bound_rect(splitted_array)
print(rectangles)
print (splitted_array)
    





"""class Tree_count:
    def __init__ (self, f_val, s_val, th_val):
        self.f_val = f_val
        self.s_val = s_val
        self.th_val = th_val
        self.rect_one = f_val
        self.rect_two = self.min_b_rect()
        
        
    def min_b_rect(self) :
        pi2 = np.pi / 2.
        point = self.trig
        # get the convex hull for the points
        hull_points = point[ConvexHull(point).vertices]

        # calculate edge angles
        edges = np.zeros((len(hull_points) - 1, 2))
        edges = hull_points[1:] - hull_points[:-1]

        angles = np.zeros((len(edges)))
        angles = np.arctan2(edges[:, 1], edges[:, 0])

        angles = np.abs(np.mod(angles, pi2))
        angles = np.unique(angles)

        # find rotation matrices
        # XXX both work
        rotations = np.vstack([
            np.cos(angles),
            np.cos(angles - pi2),
            np.cos(angles + pi2),
            np.cos(angles)]).T

        rotations = rotations.reshape((-1, 2, 2))

        # apply rotations to the hull
        rot_points = np.dot(rotations, hull_points.T)

        # find the bounding points
        min_x = np.nanmin(rot_points[:, 0], axis=1)
        max_x = np.nanmax(rot_points[:, 0], axis=1)
        min_y = np.nanmin(rot_points[:, 1], axis=1)
        max_y = np.nanmax(rot_points[:, 1], axis=1)

        # find the box with the best area
        areas = (max_x - min_x) * (max_y - min_y)
        best_idx = np.argmin(areas)

        # return the best box
        x1 = max_x[best_idx]
        x2 = min_x[best_idx]
        y1 = max_y[best_idx]
        y2 = min_y[best_idx]
        r = rotations[best_idx]

        rval = np.zeros((4, 2))
        rval[0] = np.dot([x1, y2], r)
        rval[1] = np.dot([x2, y2], r)
        rval[2] = np.dot([x2, y1], r)
        rval[3] = np.dot([x1, y1], r)
        return rval

    def areadif_first (self):
        triangle = (Polygon(self.f_val)).area
        b_rec = (Polygon(self.minrect)).area
        res = triangle / b_rec
        return res
    
 
 
 

 
 
    








l=[Treenode(points[0], 1), Treenode(points[1], 2), Treenode(points[2], 3),
Treenode(points[3], 4),
Treenode(points[4], 5),
Treenode(points[5], 6),
Treenode(points[6], 7)]"""
