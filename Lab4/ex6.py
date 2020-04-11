numToSqrt = 4
exact = numToSqrt**0.50
val = 1.4
TOL = 1e-1
iternum = 1
itermax = 1000000
while abs(val**2 - numToSqrt) > TOL and iternum < itermax:
    val = val * 1.00001
    if abs(val**2 - numToSqrt) < TOL:
        print('After {0} iterations'.format(iternum))
        print('Root is {0}'.format(val))
        print('Exact roots is {0}'.format(exact))
        break
    iternum = iternum + 1