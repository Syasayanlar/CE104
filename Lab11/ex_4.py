import matplotlib.pyplot as plt

x_data = [0.0, 2.0, 2.0, 0.0]
y_data = [0.0, 0.0, 3.3, 3.3]

n_node = len(x_data)
x_new = [0]*(n_node+1)
y_new = [0]*(n_node+1)
for i in range(n_node):
  x_new[i] = x_data[i]
  y_new[i] = y_data[i]
x_new[i+1]=x_data[0]
y_new[i+1]=y_data[0]

plt.plot(x_new, y_new, 'ko-')
plt.xlabel('x-coords')
plt.ylabel('y-coords')
plt.grid()
plt.show()