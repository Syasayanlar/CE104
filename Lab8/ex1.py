import math

myMatrix = [[1.0, -2, math.sin(math.pi/5.0)],
             [math.exp(2), 5.0/2.0, 6],
             [math.cos(math.pi/2), -6, -2]]

V = [[1, 2, 3],
     [3, 5, 6],
     [11, 2, 3]]
#1. write a function to compute the following properties of given 2D matrix
#   a. Summation
#   b. Average
#   c. Maximum value
#   d. Minimum value
#   e. Standard deviation
#   formula for standard deviation is :
#   sqrt( (1/N) * sum(x_i - ave)**2)
#   where N is # of elements
#   sum() : is summation from i=1 to N
# and return them

def operations(mat):
    r = len(mat)
    c = len(mat[0])
    
    n_el = r*c
    sum_ = 0
    max_val = 0
    min_val = 100
    for i in range(r):
        for j in range(c):
            sum_ += mat[i][j]
            
            if mat[i][j]>max_val:
                max_val = mat[i][j]
                
            if mat[i][j]<min_val:
                min_val = mat[i][j] 
    ave = sum_ / n_el
    std = 0.0
    for i in range(r):
        for j in range(c):
            std += (myMatrix[i][j]-ave)**2
    std = math.sqrt((1/n_el)*std)
    
    
    print('Sumamtion is ', sum_)
    print('Average is ', ave)  
    print('Maximum value is ', max_val)
    print('Minimum value is ', min_val)      
    print('Standard deviation is ', std)  #3.88704657509289 
    return ave, sum_, max_val, min_val, std

average_, sum_, max_val_, min_val_, std_ = operations(myMatrix)

    
   