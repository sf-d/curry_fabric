from curry_fabric.curriedfunc import curry, p
import sys
import plotly.express as px
import numpy as np


np.set_printoptions(precision=3, threshold=sys.maxsize, suppress=True)

STEPS = 15

L = p(STEPS, (5000000, 50000000))
A = p(STEPS, (1000000, 5000000))


@curry
def D_sn(L, A):
    return L / A

test_ar = D_sn(L, A)
print (test_ar)


#Целевые показатели
D_sn_goal = 15
A_goal = 2600000
L_goal = 39000000
goal_ar = np.array([L_goal, A_goal, D_sn_goal])


'for t in test_ar:'
'dist = np.linalg.norm(t- goal_ar)'
    
    


# operations with array if we have more then 3 values
"b = np.sum(a, where=[True,True,True,True, False,False], axis = 1, keepdims = True)"
'#c = np.take(a,[4,5], axis=1)'
'#result = np.append(b, c, axis=1)'


list_a=np.take(test_ar, [0], axis =1)
list_aa = list_a.flatten()

list_b = np.take(test_ar, [1], axis =1)
list_bb = list_b.flatten()

list_c = np.take(test_ar, [2], axis =1)
list_cc = list_c.flatten()

fig = px.scatter_3d(x=list_aa, y=list_bb, z=list_cc, text=range(len(list_bb)))
fig.show()
