import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 5*x  + 1
def df(x):
    return 2*x - 5

analytical_roots = [0.208712 , 4.79129]    

x0 = -2
x1 = 5
x = np.linspace(x0, x1, 100)

plt.plot(x, f(x))
plt.plot(analytical_roots[0], 0, 'k*')
plt.plot(analytical_roots[1], 0, 'r*')
plt.grid()
plt.xlabel('x-vals')
plt.ylabel('y-vals')
plt.xlim([x0, x1])
plt.show()