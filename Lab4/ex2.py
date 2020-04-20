from numpy import zeros
# for the given x values 
# i. create multiplcation table
# ii. Print on the screen
# hint : use for loop
# extra : store data in 2D matrix

limit = 10
myMat = zeros( (limit,limit) )
for i in range(limit):
    for j in range(limit):
        val = (i+1)*(j+1)
        myMat[i,j] = val

for i in range(10):
    print(i)





i_val = 6
for i in range(1, i_val+1):
    for j in range(1, i_val+1):
        print(i*j, '\t', end='') # end='' means no new line
    print()
   
data_mat = zeros((i_val, i_val))    
for i in range(i_val):
    for j in range(i_val):
        data_mat[i,j]=(i+1)*(j+1)
    
