from math import sqrt
from numpy import roots
# to find the roots of quadratic equation in the form of
# a*x**2 + b*x + c = 0
# discrimant d_ has to be computed as follows,
# d_ = b**2 - 4*a*c
# then the roots can be computed as follows
# x_i = (-b +- sqrt(d_))/(2*a)
# write a function to find the roots of any given quadratic function








def rootFinder(a,b,c):
    d_ = b**2 - 4*a*c
    x_1 = (-b + sqrt(d_))/(2*a)
    x_2 = (-b - sqrt(d_))/(2*a)
    return x_1, x_2

a, b, c = 1, -3, -6

print('Equation is {0}x**2 + {1}x + {2}'.format(a,b,c))
print('Roots are ', rootFinder(a,b,c))
        

 



