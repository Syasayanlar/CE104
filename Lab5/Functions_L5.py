def alternator(i,j,k):
    ''' alternator function
    returns 1 for positive permutations of 1,2 and 3
    returns -1 for negtavie permutations of 1, 2 and 3
    return 0 is any of i,j or k is repeteaded
    return NOTHING if i, j or k is larger than 3
    1-> 2-> 3                                                                
    alternator(1,2,3) returns 1
    alternator(2,3,1) returns 1
    alternator(3,1,2) returns 1
    alternator(1,3,2) returns -1
    alternator(2,1,3) returns -1
    alternator(3,2,1) returns -1
    '''
    if i > 3 or j > 3 or k > 3:
        print('i, j, k must be less than 3.')
        return 0
    if i == j or i == k or j == k:
        return 0
    if i <= 3 and j <= 3 and k <= 3:
        if i == 1 and j == 2 and k == 3:
            return 1
        if i == 2 and j == 3 and k == 1:
            return 1
        if i == 3 and j == 1 and k == 2:
            return 1
        if i == 1 and j == 3 and k == 2:
            return -1
        if i == 2 and j == 1 and k == 3:
            return -1
        if i == 3 and j == 2 and k == 1:
            return -1
        
def norm(myVec):
    '''
    A function returns norm of a vector
    where norm of vector b is
    (b[i]*b[i])**0.50
    '''
    el_num = len(myVec)
    sum_ = 0.0
    for i in range(el_num):
        sum_ = sum_ + myVec[i]*myVec[i]
    sum_ = sum_**0.50
    return sum_

def dyadic(v1, v2):
    '''
    Two dimensional arrays can be shown as
    A = A[i,j]* e1_dyadic_e2
    where e1 and e2 are unit vectors
    _dyadic_ is an matrix operation
    which can be defined as
    e1_dyadic_e2 = e1[i]*e2[j]
    Thus, _dyadic_ operation yields i by j matrix
    '''
    rows = len(v1)
    cols = len(v2)
    res = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            res[i][j]= v1[i]*v2[j]
    return res

def zeros(n):
    ''' 
    Function returns zero matrix with the given shape n
    if n is 3 then
    zeros(3) --> [[0,0,0],
                 [0,0,0],
                 [0,0,0]]    
    '''
    res = [[0 for i in range(n)] for j in range(n)]
    return res

def ones(n):
    ''' 
    Function returns zero matrix with the given shape n
    if n is 3 then
    zeros(3) --> [[1,1,1],
                 [1,1,1],
                 [1,1,1]]    
    '''
    res = [[1 for i in range(n)] for j in range(n)]
    return res

def identitiy(n):
    ''' 
    Function returns zero matrix with the given shape n
    if n is 3 then
    zeros(3) --> [[1,0,0],
                 [0,1,0],
                 [0,1,0]]    
    '''
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                res[i][j]=1
    return res

def primeFactors(num):
    ''' 
    For the given number num, return a list of prime factors
    ex : primeFactor(350) --> [2,5]
    '''
    if num > 0:
        if num == 1:
            return 1
        elif num == 2:
            return 2
        else:
            factors = []
            for i in range(2,num+1):
                if num%i==0:
                    factors.append(i)
                    num = num/i
            return factors
    else:
        print('Not possible in negative numbers')
        return None