from scipy.optimize import root
from scipy.misc import derivative

def f0(x):
    return x**3 + 3*x
df0 = derivative(f0, 1.0, dx=1e-6)

print('derivative of f0 at x = 1.0 : {0:.9f}'.format(df0))

def f(x):
    return x**2-5*x+3

sol = root(f, [0])
x_root = sol['x']
print('Root of equation is {0:.9f}'.format(x_root[0]))