from Functions_L5 import alternator

# Cross product of vectors
# lets say vectors e1 and e2 are defined.
# and we are asked to find a vector perpendicular to those two
# to do that cross product of e1 and e3 has to be calculated
# cross product of two vector is defiend as
# e1 x e2 = alternator*e1*e2
# or in indice form
# (e1xe2)[i] = alternator(i,j,k)*e1[j]*e2[k]
e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 0]

# So for the given vectors e1 and e2 compute e3
# Actually, e1, e2 and e3 are unit vetors in the directions of x, y and z, respectively.

# Res[i] = alternator(i,j,k)*e1[j]*e2[k]
for i in range(3):
    for j in range(3):
        for k in range(3):
            e3[i] += alternator(i+1,j+1,k+1)*e1[j]*e2[k]
