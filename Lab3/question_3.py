# write a list which consists of the letters in your name
# nameList = ['a', 'l', 'i']
# then for each eleement check if it is vowel or not
# hits:
# 1. create a list contains vowels  (a,e,ı,i,u,ü,o,ö)
# 2. DONT USE ı,İ,ö,Ö,Ü,ü 
# 3. loop over letters of your name, check if it is vowel or not

#vowels = ['a', 'e', 'i', 'u', 'o']
#name = ['u', 's', 't', 'u', 'n']
#
#for char in name:
#    for vow in vowels:
#        if char is vow:
#            print('{0} is vowel'.format(char))



myName = 'sUlEymAn'.lower()
vowel = 'aeiuo'.lower()

for char in myName:
    for voe in vowel:
        if char is voe:
            print(char)
    