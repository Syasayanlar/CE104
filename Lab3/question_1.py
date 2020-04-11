# create 1D list with 1000 elements which consists of element in range 1, pi
# create a 3by4 matrix (A)
# take tranpose (A_T)
# multiplication of first row second element and last row last element
# create 100by100 matrix whose diagonal is one and other elements are 0


import numpy as np

#my1D_list = np.arange(1, np.pi, 0.05) # evenly spaced
my1D_list = np.linspace(1, np.pi, 1000)

A = np.matrix([[1,2,3],
                   [4,6,7],
                   [0, -1, 2]])

A_T = np.transpose(A)


res = A[0,1]*A[-1,-1]

eye_mat = np.eye(100)



