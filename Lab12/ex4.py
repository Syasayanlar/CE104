import sympy as sp

x, y= sp.symbols('x, y')
# eq1 = -x + y - 1
# eq2 = x + y - 3
# sol_L= sp.linsolve([eq1, eq2], [x, y]) 
# print(sol_L)

eqNL_1=x**2-2*y
eqNL_2=x+y**2-3
sol_NL = sp.nonlinsolve( [eqNL_1, eqNL_2] , [x, y])
print(sol_NL)
