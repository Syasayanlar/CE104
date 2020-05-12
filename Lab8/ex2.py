myMat = [1, 0, -1, 5, 9, 7, 100]
# sort the given array in ascending order
# the result has to be [ 9, 7, 5, 0, 1, -1]
def sortArr(arr, flag):
    c = len(myMat)
    if flag == 1:
        str_ = 'ascending'
    elif flag == -1:
        str_ = 'descending'
        
    for i in range(c):
        for j in range(i+1,c):
            if flag == 1: # ascending order
                if myMat[i] < myMat[j]:
                    temp = myMat[i]
                    myMat[i] = myMat[j]
                    myMat[j] = temp    
            elif flag == -1: #descending order
                if myMat[i] > myMat[j]:
                    temp = myMat[i]
                    myMat[i] = myMat[j]
                    myMat[j] = temp     
    print('Matrix in '+str_+' order: ')   
    print(arr)     
    
sortArr(myMat, 1)   