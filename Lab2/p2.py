from math import pi

myList_2D = [ [1.234, 2.534, pi],
        [-4.3, 5, 6],
        [7, 8, 9.7] ]

##print('First row second element : {0}'.\
##      format(myList_2D[0][1]))

mL_11 = myList_2D[0][0]
mL_13 = myList_2D[0][2]

summation = mL_11 + mL_13
difference = mL_11 - mL_13
mulitply = mL_11 * mL_13
division = mL_11 / mL_13

resArray = [] # This is an empty array

# by using APPEND command add summation ... division to list
resArray.append(summation)




