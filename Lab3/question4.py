# create a list contains the numbers in your school number
# calcualte the summation of the numbers
# if number is 234567 then list [2, 3, 4, 5, 6, 7]
# summation has to be 27
# summation of numbers divisible by 7

#myNum = ['2', '3', '4', '5', '6', '7']
myNum = [2, 3, 4, 5, 6, 7]

sum_ = 0
for num in myNum:
    if num%7==0:
        sum_ = sum_ + num













myNum = input('Enter number :')
summation = 0
divSum = 0
for el in myNum:
    summation = summation + float(el)
    if float(el)%7==0:
        divSum = divSum + float(el)