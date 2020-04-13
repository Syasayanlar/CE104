# for the range of x = 0, 956 with the increment of 2
# compute the summation of f(x) = (x**3-x)/(x*(x-2))  
# can be downloaded from https://github.com/Syasayanlar/CE104/archive/master.zip
def f_(x):
    res = (x**3-x)/(x*(x-2))
    return res

x = 0
sum1 = 0
while x < 956:
    if x == 2 or x == 0:
        print('At x = {0} division by zero.'.format(x))
        x = x + 2
        continue
    else:
        sum1 += (x**3-x)/(x*(x-2))
#        sum1 += f_(x)
    x = x + 2
    
print('Summation is : ', sum1)     