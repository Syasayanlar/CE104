import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# define an equations by using a SYMBOLIC variable
x = sp.Symbol('x')
eq = x*(x**3-sp.sin(sp.pi/36)*x)
print(eq)

# Using solve function to solve it wrt that variable
solution = sp.solvers.solve(eq)
print(solution)

# Compute derivative of SYMBOLIC function
diff_1 = sp.diff(eq, x)
print(diff_1)

#Lets convert to numeric functions
def eq_num(x):
  return x*(x**3 - x*np.sin(np.pi/36))

def diff_eq_num(x):
  return  x**3 + x*(3*x**2 - np.sin(np.pi/36)) - x*np.sin(np.pi/36)

n_node = 150
x = np.linspace(1, 5, n_node)
fx = np.zeros(n_node)
dx = np.zeros(n_node)
for i in range(len(x)):
  fx[i]=eq_num(x[i])
  dx[i]=diff_eq_num(x[i])

plt.plot(x, fx, label='function')
plt.plot(x, dx, label='First derivative')
plt.grid()
plt.legend()
plt.xlabel('x-data')
plt.ylabel('y-data')
plt.tight_layout()
plt.savefig('Last example')
plt.show()
# eq = (x**3+6*x**2)*sp.sin(sp.pi/x)
# root_eq = sp.root(eq,3)
# print(eq)
