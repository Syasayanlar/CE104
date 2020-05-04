def f(x):
    return x**2-5*x+3

#The Bisection algorithm:
#1- Input the values of x where root is expected to be in between
#1.1- Define max_iter and tol    
#2- Compute the function values for those x values (x0, x1)
#3- Check if the signs of functions at x0 and x1
#4- If signs are the same stop and change the x values
# START LOOP
#5- compute xh = 0.50*(x0+x1)
#6- compute function values for x0, x1 and xh (y0, y1, yh)
#7- If y0*yh < 0 then x1 = xh
#8- Else x0 = xh
#9- If the values of y approaches zero, print the x-value and stop
#10- Else repeat steps 5 to 10


#1. while loop
x0 = -1
x1 = 3

max_iter = 100
tol = 1e-9

y0 = f(x0)
y1 = f(x1)
isConverged = False
i=1
while abs(y0)>tol and i < max_iter:
    if y0*y1 > 0:
        print('No root in the interval.')
        break
    else:
        xh = 0.50 * (x0+x1)
        yh = f(xh)
        y0 = f(x0)
        y1 = f(x1)
        if y0*yh < 0:
            x1 = xh
        else:
            x0 = xh
        if abs(y0)<tol:
            isConverged = True
            print('Root of equation is {0:.9f} and found in {1:d} iterations.'\
           .format(x0, i))
            break
        i += 1
        
if isConverged is False:
    print('Root of equation is not found after {0:i} iterations.'\
           .format(i))
            
#2. for loop    
x0 = -1
x1 = 3

max_iter = 100
tol = 1e-9

y0 = f(x0)
y1 = f(x1)

if y0*y1 > 0:
    print('No root in interval.')
    print('define interval again')

for i in range(1, max_iter+1):
    xh = 0.50*(x0+x1)
    yh = f(xh)
    y0 = f(x0)
    y1 = f(x1)
    
    if y0*yh < 0:
        x1 = xh
    else:
        x0 = xh
        
    if abs(y0) < tol:
        print('Root of equation is {0:.9f} and found in {1:d} iterations.'.format(x0, i))
        break
    
    
    
    
    
    
    