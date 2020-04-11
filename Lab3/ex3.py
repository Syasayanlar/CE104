import numpy as np

myNum = 19
if myNum > 0:
    if myNum%2==1:
        print('Odd number')
    else:
        print('Even number')
else:
    print('Not defined in negative numbers')
    
myPoint = -100

if myPoint > 0.0 and myPoint <= 100:
    if myPoint >= 80:
        grade = 'AA'
    elif myPoint < 80 and myPoint >= 75:
        grade = 'BB'
    elif myPoint < 75 and myPoint >= 50:
        grade = 'CC'
    else:
        grade = 'FF'
else:
    grade = 'NA'
    print('Not defined')
    
print(grade)

myList = np.linspace(5, 100, 20)
elNum = len(myList)

for el in myList:
    print(el)

for i in range(elNum):
    print('This is elemenet #',i, 'and value is', myList[i])
          
phrases = ['let\'s', 'do', 'an', 'example']

for word in phrases:
    print(word)


