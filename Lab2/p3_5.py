import numpy as np

myList1 = np.linspace(1, 100, 9)
myList2 = np.matrix('2 4 5; 2 34 5.6; 2.3 4.5 1')

#type(myList1)
# second row, second element of myList2 is what ??

myList1Shaped = myList1.reshape(3,3)
myList2Shaped = myList2.reshape(9,1)