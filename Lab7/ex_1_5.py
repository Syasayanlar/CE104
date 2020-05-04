nums = [1, 5, 0, 3, 23, -10]


'''Write a script that returns
    1. Maximum of given array
    2. Minimum of given array'''
    
max_ = 1    # assumed max value
for el in nums: # loop over nums
    if el > max_: # check if it is max or not
        max_ = el # if it is max assign new value
        
        
min_ = 100    # assumed max value
for el in nums: # loop over nums
    if el < min_: # check if it is min or not
        min_ = el # if it is min assign new value        

max_ = 1
for i in range(len(nums)):
    if(nums[i]>max_):
        max_ = nums[i]
        
        
min_ = 100
for i in range(len(nums)):
    if(nums[i]<min_):
        min_ = nums[i]
        
        
''' Do the same thing for 2D matrices'''
nums2D = [ [ 1,    5,   0],
           [ 3,   23, -10],
           [-3, -100, 909] ]
r = len(nums2D)
c = len(nums2D[0])

max_2D = 1
min_2D = 100
for i in range(r):
    for j in range(c):
        if nums2D[i][j] > max_2D:
            max_2D = nums2D[i][j]
        if nums2D[i][j] < min_2D:
            min_2D = nums2D[i][j]


r = len(nums2D)
c = len(nums2D[0])
max2d = 1
min2d = 100
for i in range(r):
    for j in range(c):
        if nums2D[i][j]>max2d:
            max2D = nums2D[i][j]
        elif nums2D[i][j]<min2d:
            min2d = nums2D[i][j]

        
