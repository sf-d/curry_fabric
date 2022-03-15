from curry_fabric.curriedfunc import curry, p
import sys
from shapely.geometry import MultiPoint, Polygon, LineString
import plotly.graph_objects as go
from scipy.spatial import ConvexHull
import numpy as np

points =   np.asarray([[[661.0, 249.0], [750.0, 274.0], [635.0, 276.0]], 
            [[706.0, 355.0], [635.0, 276.0], [750.0, 274.0]], 
            [[706.0, 355.0], [750.0, 274.0], [778.0, 334.0]], 
            [[778.0, 334.0], [672.0, 398.0], [706.0, 355.0]], 
            [[606.0, 492.0], [672.0, 398.0], [747.0, 511.0]], 
            [[598.0, 428.0], [672.0, 398.0], [606.0, 492.0]], 
            [[778.0, 334.0], [747.0, 511.0], [672.0, 398.0]]])


# key = list of all points of every minimum polygon 
# нужно разделить предарительно лист всех точек на отдельные полигоны

class Treenode:
    
    def __init__(self,points_list, key):
        self.trig = points_list
        self.left = None
        self.right = None
        self.place = key
        self.minrect = self.min_b_rect()
        self.area = self.areadif()

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

    def areadif (self):
        triangle = (Polygon(self.trig)).area
        b_rec = (Polygon(self.minrect)).area
        res = triangle / b_rec
        return res


# функция написания дерева, в котором предполагается объединение нескольких элементов  

#def tree_func(first_el, sec_el, th_el):
    
 #   return 

l=[Treenode(points[0], 1), Treenode(points[1], 2), Treenode(points[2], 3),
Treenode(points[3], 4),
Treenode(points[4], 5),
Treenode(points[5], 6),
Treenode(points[6], 7)]
for i in l: 
    print (i.area)