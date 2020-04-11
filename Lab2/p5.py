from numpy import pi

for i in range(10):
    print('This is i : {0}'.format(i))
    
for i in range(5, 20):
    print('This is i : {0}'.format(i))

myList = []
for i in range(7,20,3):
    print('This is i : {0}'.format(i))
    myList.append(i*pi)
    
# print the elements of myList, use for loop
# or do it one by one