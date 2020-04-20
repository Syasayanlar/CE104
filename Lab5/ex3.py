import numpy as np
from Functions_L5 import dyadic
#    Two dimensional arrays can be shown as
#    A = A[i,j]* e1_dyadic_e2
#    where e1 and e2 are unit vectors
#    _dyadic_ is an matrix operation
#    which can be defined as


#    e1_dyadic_e2 = e1[i]*e2[j]
#    Thus, _dyadic_ operation yields i by j matrix
e1 = [1, 0, 0]
e2 = [0, 1, 0]

rows = len(e1)
cols = len(e2)
res = [[0 for i in range(rows)] for j in range(cols)]
for i in range(rows):
    for j in range(cols):
        res[i][j] = e1[i]*e2[j]

print('result of OUR function {}'.format(dyadic(e1,e2)))
print('result of NUMPY function {}'.format(np.outer(e1,e2)))