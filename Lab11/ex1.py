import matplotlib.pyplot as plt
import numpy as np

def draw_tr(x_coords, y_coords, d_type):
  n_node = len(x_coords)
  x_new = [0]*(n_node+1)
  y_new = [0]*(n_node+1)
  for i in range(n_node):
    x_new[i] = x_coords[i]
    y_new[i] = y_coords[i]
  x_new[i+1]=x_coords[0]
  y_new[i+1]=y_coords[0]

  plt.plot(x_new, y_new, d_type)
  # plt.show()


x_coords = np.array([1.0, 2.3, 0.0])
y_coords = np.array([0.0, 4.4, 6.0])
x_coords2 = np.array([3.5, 2.3, 0.0])
y_coords2 = np.array([0.0, 2.4, 6.0])
x_coords3 = np.array([0.5, 2.3, 0.0])
y_coords3 = np.array([0.0, 4.4, 2.0])
x_coords4 = np.array([3.0, 2.4, 0.3])
y_coords4 = np.array([0.6, 4.7, 6.0])

# First plot all yhe points
plt.plot(x_coords[0], y_coords[0], 'r*')
plt.plot(x_coords[1], y_coords[1], 'g*')
plt.plot(x_coords[2], y_coords[2], 'k*')
# plt.show()

# Lets draw a triangle
x_coords_tr = np.array([1.0, 2.3, 0.0, 1.0])
y_coords_tr = np.array([0.0, 4.4, 6.0, 0.0])
plt.plot(x_coords_tr, y_coords_tr, '-o')
# plt.show()
d_type = 'k-o'
draw_tr(x_coords, y_coords, d_type)
# plt.show()
# now write a function that draws triangle for given data 
# x_coords and y_coords must be input


