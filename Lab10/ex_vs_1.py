import numpy as np
import matplotlib.pyplot as plt

# lets define a function and its first derivative
def f(x):
    return x**2 - 5*x  + 1

# analytical roots can be computed easily please check ex_vs_4
analytical_roots = [0.208712 , 4.79129]    


# define a range where the roots are known to be existing
x0 = -2
x1 = 5
x = np.linspace(x0, x1, 100)


# plot f(x) and its roots
plt.plot(x, f(x), label='f(x)')
plt.plot(analytical_roots[0], 0, 'k*', label='root #1')
plt.plot(analytical_roots[1], 0, 'r*', label='root #2')
plt.grid()
plt.xlabel('x-vals')
plt.ylabel('y-vals')
plt.xlim([x0, x1])
plt.tight_layout()
plt.legend()
plt.savefig('myfig')
plt.show()