from functions import printMatrix

def createMatrix(r, c):
    ''' creates r by c matrix
    where all even numbered rows get 1 and
    all odd numbered rows get value of -1
    even though inedx number starts with 0
    for this example 1st row is ROW 1
    createMatrix(3, 2)
    
    [[-1, -1], [1, 1], [-1, -1]]
    '''
    result = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if (i+1)%2 == 0:
                result[i][j]=1
            else:
                result[i][j]=-1
    return result

def createStingMatrix(str_inp):
    ''' A function prints strings input argument
    returns None
    str_inp : input in string format'''
    
    myMat = str_inp.split()
    r = len(myMat)
    for i in range(r):
        print(myMat[i])
    return None

myString = "HeLLo hoW are yoU".lower()
createStingMatrix(myString)
interestingMatrix = createMatrix(3,2)
printMatrix(interestingMatrix, 'Matrix is :')
                