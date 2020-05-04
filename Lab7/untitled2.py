# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:46:56 2020

@author: suley
"""

x0 = -1
x1 = 3
max_iter = 100
tol = 1e-12

y0 = f(x0)
y1 = f(x1)

#1. for loop
if y0*y1>0:
    print('No root in interval')
for i in range(max_iter):
    xh = 0.5*(x0+x1)
    yh=f(xh)
    y0=f(x0)
    if abs(y0) < tol:
        print('Root is :', x0)
        print('# of iterations :', i+1)
        break
    elif y0*yh < 0:
        x1 = xh
    else:
        x0 = xh