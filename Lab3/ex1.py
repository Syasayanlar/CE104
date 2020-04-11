import numpy as np

# creating 1d and 2d arrays
my1DArray = [1, 2.3, 4.5, -2, np.pi]
my2DArray = [ [1, 2, 3**(2.4)],
             [-1, -20.2, np.exp(3)],
             np.sin(np.pi), np.tanh(np.pi), -2.0] 

# elements of arrays
firstElement = my1DArray[0]
lastElement = my1DArray[-1]

firstRowFirstCol = my2DArray[0][0]
secondRowThirdCol = my2DArray[1][2]

partOfmy1DArray = my1DArray[1:3]
partOfMy2DArray = my2DArray[:][2]

# convert the arrays into numpy arrays
numpyAr1D = np.array(my1DArray)
numpyAr2D = np.matrix(my2DArray)

