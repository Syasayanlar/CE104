def f(x):
    sol = x**3 + 3*x
    return sol

def df(x):
    return 3*x**2 + 3


#Using forward difference formula find the first
#derivative of function f(x)
#Forward difference formula is as follows
# f'(x_i) = f(x_(i+1)-f(x_i)) / (x_(i+1)-x_i)
h = 1e-6    
x_1 = 1

x_2 = x_1 + h
# using forward diff:
df_FD = (f(x_2)-f(x_1)) / (x_2-x_1)
                                                                                    
# Backward difference formula is as follows
# f'(x_i) = f(x_(i)-f(x_i-1)) / (x_(i)-x_(i-1)
x_0 = x_1 - h
df_BD = (f(x_1)-f(x_0))/(x_1-x_0)

# Central difference formula is as follows
# f'(x_i) = f(x_(i+1)-f(x_(i-1)) / (x_(i+1)-x_(i-1)
x_0 = x_1 - h
x_2 = x_1 + h
df_CD = (f(x_2)-f(x_0))/(x_2-x_0)

print('Analytical value : {0:.9f}'.format(df(x_1)))
print('Forward Derivative : {0:.9f}'.format(df_FD))
print('Backward Derivative : {0:.9f}'.format(df_BD))
print('Central Derivative: {0:.9f}'.format(df_CD))

# now write a function, which get function values at points
# and points values,
# then returs central derivative value
# ex : diff_( func_vals, x_vals) --> df

def diff_(func_vals, x_vals):
    x0 = x_vals[0]
    x2 = x_vals[1]
    fx0 = func_vals[0]
    fx2 = func_vals[1]
    df = (fx2-fx0)/(x2-x0)
    return df

xi = 1
h = 1e-3
x0 = xi-h
x2 = xi+h
x_vals = [x0, x2]
func_vals = [f(x0), f(x2)]
print('Derivative in function : {0:.9f}'.format(diff_(func_vals, x_vals)))