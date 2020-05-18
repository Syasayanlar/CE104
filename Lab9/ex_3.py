A = [[-1, -3, 3, 5, 6],
     [-4, -3, 0, 5, 6],
     [-6, -3, 3, 5, -1],
     [-7, 0, 3, 5, -2],
     [-1, -3, 2, 0, 6]]

# write a function to return the summation of positive numbers, negative numbers
# and repetattion of zeros in any 2d Matrix
# doOperations(A) --> num_zeros = 3, sum_neg = -34, sum_pos 49        
def doOperations(A):
    sum_pos = 0
    sum_neg = 0
    num_zeros = 0
    for r in A:
        for el in r:
            if el == 0:
                num_zeros += 1
            elif el < 0:
                sum_neg += el
            elif el > 0:
                sum_pos += el
                
    return num_zeros, sum_neg, sum_pos

print(doOperations(A))

nz, sn, sp = doOperations(A)
                
                
                
                
                
                
                
                
                