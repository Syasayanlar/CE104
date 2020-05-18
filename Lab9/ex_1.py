cols = 3
rows = 2
myMat = [[i*j for i in range(cols)] for j in range(rows)]

print('This is myMat', myMat)

# write a function to change any specific value in matrix to input
# if A = [[0, 0, 0], [1,2,3]]
# changeIt(A, 0, 3) must return [[3, 3, 3],[3,2,3]]

def changeIt(A, old, new):
    rows = len(A)
    cols = len(A[0])
    B = [[0 for i in range(cols)]for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == old:
                B[i][j] = new
            else:
                B[i][j]=A[i][j]
                
    return B

print( changeIt(myMat, 0, 3) )
            
            
            
            
            
            