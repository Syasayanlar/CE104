n1 = float(input('Enter number 1: '))
n2 = float(input('Enter number 2: '))
#n1 = 23.445782732
#n2 = 234.53434

if n1>n2:
    print('{0} is larger than {1}'\
          .format(n1, n2))
elif n2>n1:
    print('{0} is larger than {1}'\
          .format(n2, n1))
else :
    print('{0} is equal {1}'\
          .format(n1, n2))
    
# to the same for checking the ABSOLUTE VALUE
# of two numbers
# USE BUILT-IN abs() function
# type '? abs' to see how to use it