import numpy as np
from matplotlib import pyplot as plt

limit = int(input('Enter the limit value'))

myList = np.zeros((limit,1))
myList2 = np.zeros((limit,1))
myList3 = np.zeros((limit,1))
for i in range(limit):
    a = i*np.pi/16
    b = np.cos(a)
    c = np.sin(a)
    myList[i]=a
    myList2[i]=b
    myList3[i]=c
    print('{0:2f} is added to list'.format(a))
    
plt.plot(myList, myList2, label='Cos')
plt.plot(myList, myList3, label='Sin')
plt.grid()
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('cosine diagram')
plt.legend()
plt.show()