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