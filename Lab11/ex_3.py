import numpy as np
import matplotlib.pyplot as plt
def fx(x):
  return 3*x**3+x**2.0+2.0*x-5

def df(x):
  return 9*x**2+2*x+2

def ddf(x):
  return 18*x+2

x_data = np.linspace(1,5,100)
y = fx(x_data)
dy = df(x_data)
ddy = ddf(x_data)

plt.subplot(311)
plt.plot(x_data, y)
plt.xlabel('x-data 1')
plt.ylabel('y-data 1')
plt.title('plot 1')
plt.xlim([1, 5])
plt.grid()

plt.subplot(312)
plt.plot(x_data, dy)
plt.xlabel('x-data 1')
plt.ylabel('y-data 2')
plt.title('plot 2')
plt.xlim([1, 5])
plt.grid()

plt.subplot(313)
plt.plot(x_data, dy)
plt.xlabel('x-data 3')
plt.ylabel('y-data 3')
plt.title('plot 3')
plt.xlim([1, 5])
plt.grid()

plt.tight_layout()
plt.savefig('myPlot.png')

plt.show()

