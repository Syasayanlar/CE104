import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 5*x  + 1
def df(x):
    return 2*x - 5

# First find roots by using numpy.
# to do that roots functions is used    
coeffs = [1, -5, 1] 
x_roots = np.roots(coeffs)

print('The roots are {0:.5f}, {1:.5f}'.format(x_roots[0], x_roots[1]))

# now compute the roots by using newton's method
# x_new = x_n - f(x_n)/df(x_n)
# while the ||x_new - x_n || > TOL 
#    x_new must be computed

TOL = 1e-5
diff = 1
x_n = -3
iter_ = 0
while abs(diff) > TOL:
    x_new = x_n - f(x_n)/df(x_n)
    diff = x_new - x_n
    if diff < TOL:
        f_converged = True
    iter_ += 1
    if iter_ > 1000:
        print('Not converged after {0:d} steps'.format(iter_))
        break
    x_n = x_new
    
if f_converged == True:
    print('Root found at {0:5f}'.format(x_new))

# now put newtons method into function format
def newton(x_n, TOL=1e-6, max_iter=1000):
    diff = 1
    iter_ = 0
    while abs(diff) > TOL and iter_ < max_iter:
        x_new = x_n - f(x_n)/df(x_n)
        iter_ += 1
        diff = x_new - x_n
        # if diff < TOL:
        #     f_converged = True
        # if iter_ == max_iter:
        #     f_converged = False
        x_n = x_new
    return x_n

root1 = newton(-3)
root2 = newton(10)

# now plot the function and roots
x0 = -2
x1 = 5
num_node = 100
x = np.linspace(x0, x1, num_node)



plt.plot(x,f(x), label='Fuction x^2-5x+1')
plt.plot(root1, 0, 'rd', label='Root 1:'+str(root1) )
plt.plot(root2, 0, 'ko', label='Root 2:'+str(root2) )
plt.xlim([x0, x1])
plt.grid()
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
