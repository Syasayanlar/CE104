import numpy as np
start = 1
end = 9
noEl = 9
d_inc = 1

#start = int(input('Enter start value : '))
#end = int(input('Enter end value : '))
#noEl = int(input('How many points b/w them : '))

linspaceList = np.linspace(start, end, noEl)

#d_inc = int(input('Enter increment : '))
arrangeList = np.arange(start, end, d_inc)

# similar to Matlab syntax
numpyMatrix1 = np.matrix('1,2,3; 4,5,6; 7,8,9')
numpyMatrix2 = np.matrix('1 2 3;\
                          4 5 6;\
                          7 8 9')

# using 2D lists are more convinient
numpyMatrix3 = np.matrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
# creating 5by4 matrix
numpyMatrix4 = np.matrix([[1, -2, 0.30, np.pi, 2.3],
                          [np.cos(np.pi/3.0), 0, 0, 2, 1 ],
                          [2, 3-4, 1, 5/2, 2**2],
                          [np.cos(np.pi/3.0), 0, 0, 2, 1 ] ])
# converting it into 2by10 matrix
numpyMatrix5 = np.reshape(numpyMatrix4, (2,10) )

# transpose of a matrix
numpyMatrix5_T = np.transpose(numpyMatrix5)

#Identity, zero and one matrices can be defined by means of numpy
eyeMat = np.eye(3)
identMat = np.identity(5)
zeroMat = np.zeros((6,6))
onesMat = np.ones((6,6))