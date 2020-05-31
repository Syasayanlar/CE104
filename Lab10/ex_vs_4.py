import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,c):
    return a*x**2 + b*x  + c*1

def df(x,a,b):
    return a*x + b

def newton(x_n, a, b, c, TOL=1e-6, max_iter=1000):
    diff = 1
    iter_ = 0
    while abs(diff) > TOL and iter_ < max_iter:
        x_new = x_n - f(x_n,a,b,c)/df(x_n,a,b)
        iter_ += 1
        diff = x_new - x_n
        x_n = x_new
        if iter_ == max_iter:
            print('Not found')
            return 0, iter_
    return x_n, iter_

a = [1, 2, 3, 4, 5, 2]
b = [-5, -6, -7, 8, -8, -9]
c = [1, 3, 4, 1, 2, 1]
x_n = 0
result_file = open("results.txt", 'w')
for i in range(len(a)):
    result_file.write('Equation is {0}x**2 + {1}x + {2}\n'.format(a[i], b[i], c[i]))
    root1, iter_ = newton(x_n, a[i], b[i], c[i])
    result_file.write('root : {0:.5f}, iterations : {1}\n'.format(root1, iter_))
result_file.close()    
