from Functions_L5 import norm
import numpy as np
# compute the norm of any vector
# norm of vector b is
#    (b[i]*b[i])**0.50

a = [1, 4, 5]

print( 'Result of our funct is {}'.format(norm(a)))
print( 'Result of NUMPY funct is {}'.format(np.linalg.norm(a)))