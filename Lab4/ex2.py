# for the given x values 
# i. create multiplcation table
# ii. Print on the screen
# hint : use for loop














i_val = 8

for i in range(1, i_val+1):
    for j in range(1, i_val+1):
        print(i*j, '\t', end='') # end='' means no new line
    print()