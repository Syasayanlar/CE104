def transpose(A):
    ''' Function returns the transpose of given matrix
    A = [[1,2,3], [4,5,6]]   
    transpose(A) -> [[1,4],[2,5],[3,6]]'''
    row = len(A)
    col = len(A[0])
    
# [[0 for i in range(3)] for j in range(4)] 
# returns 4 rows and 3 coloumns    
    Atrans = [[0 for i in range(row)] for j in range(col)]
    
    for i in range(row):
        for j in range(col):
            Atrans[j][i] = A[i][j]
    return Atrans
  
def printMatrix(A, statement='Given matrix :'):
    ''' Function returns NOTHING. Only prints the given matrix
    with given statement. If not provided statement get the
    value of 'Given matrix :'''

    row = len(A) # returns number of rows in A
    col = len(A[0]) # returns number of elements in 1st row of A
    # It is number of coloumns
    print(statement)
    for i in range(row):
        for j in range(col):
            print(A[i][j],' ', end='')
        print(' ')
    return None
    
def matMul(A, B):
    ''' A fucntion returns result of the multiplication of
    two dimendional matrices.
    A : matrix
    B : matrix
    returns C
    C[i,k]=A[i,j]*B[j,k]'''
    A_row = len(A)
    A_col = len(A[0])    
    
    B_row = len(B)
    B_col = len(B[0])      
    
    # [[0 for i in range(3)] for j in range(4)] 
    # returns 4 rows and 3 coloumns    
    result = [[0 for i in range(A_row)] for j in range(B_col)]
#    result =[[]]
    if A_col != B_row:
        print('Matrix sizes are not consistent')
        return None
    else:
        for i in range(A_row):
            for k in range(B_col):
                for j in range(A_col):
                    result[i][k] += A[i][j]*B[j][k]
        return result
    
    
A = [[1,0,0],[0,1,0]]
B = [[1,5],[2,6],[3, 4]]

A_trans = transpose(A)
printMatrix(A, 'A matrix :')      
printMatrix(A_trans, 'Transpose of A matrix :') 
C = matMul(A, B)
printMatrix(B, 'B matrix :')
printMatrix(C, 'A*B: ')     






   