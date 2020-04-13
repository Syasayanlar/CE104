from numpy import zeros
# for the given x values 
# i. create multiplcation table
# ii. Print on the screen
# hint : use for loop
# extra : store data in 2D matrix
i_val = 6
for i in range(1, i_val+1):
    for j in range(1, i_val+1):
        print(i*j, '\t', end='') # end='' means no new line
    print()
   
data_mat = zeros((i_val, i_val))    
for i in range(i_val):
    for j in range(i_val):
        data_mat[i,j]=(i+1)*(j+1)
    
