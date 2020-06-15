import matplotlib.pyplot as plt
import numpy as np
from ex1 import draw_tr

x_coords = np.array([1.0, 3, 0.0])
y_coords = np.array([2.0, 4, 6.0])
x_coords2 = np.array([3.0, 5, 0.0])
y_coords2 = np.array([4.0, 6, 6.0])
x_coords3 = np.array([5.0, 7, 0.0])
y_coords3 = np.array([6.0, 8, 2.0])
x_coords4 = np.array([7.0, 9, 0.3])
y_coords4 = np.array([8.0, 0, 6.0])

draw_tr(x_coords, y_coords,'k-o')
draw_tr(x_coords2, y_coords2,'r-d')
draw_tr(x_coords3, y_coords3,'b-o')
draw_tr(x_coords4, y_coords4,'g-o')
plt.show()