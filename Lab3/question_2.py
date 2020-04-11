# create a list b/w 20, 1000, with the increment of 13
# for each element print if the element is even or odd 
# (Hint you will use for loop over elements, and for each element if condition)
import numpy as np
myList = np.arange(20, 1000, 13)

for el in myList:
    if el%2==0:
        print('{0} is even.'.format(el, 2323, 45))
    else:
        print('{0} is odd'.format(el))