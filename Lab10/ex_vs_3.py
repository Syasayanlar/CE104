import sympy as sp
from math import sqrt

x = sp.Symbol('x')
y = sp.Symbol('y')

myEq = x**3 - 2*x**2 - 5*x  + 1

print('f(x): ', myEq)
print('df: ', sp.diff(myEq) )
print('Roots: ', sp.solve(myEq) )