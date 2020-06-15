import numpy as np
import matplotlib.pyplot as plt
def u_func(x, L, P, E, I):
  return (-0.0625*L**2*P*x + 0.0833333333333333*P*x**3)/(E*I)

x = 5
L = 100
P = -100e3
E = 2e5
I = 1e6

scale_factor = 100
a = u_func(x, L, P, E, I)
print('Displacement at x={0} is {1}mm'.format(x,a))

n_nodes = 250
x = np.linspace(0,1000,n_nodes)
u = np.zeros(n_nodes)
plt.plot(x,u,label='undeformed')
for i in range(len(x)):
  u[i]=u_func(x[i], L, P, E, I)

plt.plot(x, u, label='deformed')
plt.legend()
plt.grid()
plt.xlabel('x-coord (mm)')
plt.xlabel('Displacement (mm)')
plt.savefig('HW#2')
plt.show()



