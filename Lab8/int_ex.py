def f(x):
    return x**2+2*x

# trapezoidal rule : int(f)from a to b 
# (b-a)* (f(a)+f(b))/2
# details : https://en.wikipedia.org/wiki/Trapezoidal_rule
    
a = 2.00
b = 2.01
int_ = (b-a)*(f(a)+f(b))/2