import sympy as sp
from math import sqrt

x = sp.Symbol('x')

myEq = x**2 - 5*x  + 1

toPrint = sp.diff(myEq)

sp.solve(myEq)