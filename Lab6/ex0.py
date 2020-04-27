def sumMat(A):
    ''' Function return the summation of 
    elements in matrix
    A = [[1,2],[2,3],[3,4]]
    '''
    sum_ = 0
    r = len(A)
    c = len(A[0])
    for i in range(r):
        for j in range(c):
            sum_ += A[i][j]
    return sum_

def sumMat2(A):
    ''' Function return the summation of elements in matrix'''
    sum_ = 0
    for rows in A:
        for cols in rows:
            sum_ += cols
    return sum_

def multEl(A):
    ''' Function return the multiplication of elements in matrix'''
    prod = 1
    for rows in A:
        for cols in rows:
            prod *= cols
    return prod

def sumMatrices(A, B):
    ''' Function returns summation of two matrices
    Let A, B and C be two 2D matrices. Then summation of
    A and B can be computed as
    C[i][j]=A[i][j]+B[i][j]
    
    '''

    A_row = len(A)
    A_col = len(A[0])
    B_row = len(B)
    B_col = len(B[0])

    
    res = [[0 for i in range(A_col)] for j in range(A_row)]
    
    
    
    if A_row != B_row or A_col != B_col:
        print('Matrices are not consistent')
        return None
    else:
        for i in range(A_row):
            for j in range(A_col):
                res[i][j]= A[i][j] + B[i][j]
                
    return res


A = [[1,2,3],[4,5,6]]


sumMat(A)
sumMat2(A)
multEl(A)
sumMatrices(A, A)