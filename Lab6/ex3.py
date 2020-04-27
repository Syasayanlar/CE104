from functions import printMatrix, transpose
# lets find the number of repeats of given element in following matrix


myArray = [[3, 4, 5],[5, 6, 7], [1, 1, 3], [3, 4, 6]]

transMyArray = transpose(myArray)
r = len(myArray)
c = len(myArray[0])


num = 3
occurance = 0
for i in range(r):
    for j in range(c):
        if myArray[i][j]==num:
            occurance += 1
        else:
            continue


printMatrix(myArray, '\nmyArray :')   
printMatrix(transMyArray, '\nTranspose of myArray :')   
print('\nOccurance of {} is {}'.format(num, occurance))