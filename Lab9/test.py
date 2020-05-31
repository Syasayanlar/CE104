matrice_1=[5, 3, 1, 3, 9, 2, 6, 9]
matrice_2=[]
   
 
max_=matrice_1[0]
lenght=len(matrice_1)
i=0
 
while i <= lenght:
    for j in range(lenght): 
        max_=matrice_1[0]
        if matrice_1[j]>=max_:
            max_=matrice_1[j]
            matrice_1[j] = 0
        else:
            continue

    matrice_2.append(max_)
    i+=1
   
 
print(matrice_2)