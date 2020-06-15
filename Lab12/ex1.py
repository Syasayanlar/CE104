import sympy as sp

# x = sp.Symbol('x')
# P = sp.Symbol('P')
x, P = sp.symbols('x, P')
M = P*0.5*x
E = sp.Symbol('E')
I = sp.Symbol('I')
L = sp.Symbol('L')
c1 = (-P*L**2)/16
c2 = 0.0

eq = M #EI*d2(u)/d(x2)
print(eq)

eq1=sp.integrate(eq, x)+c1
eq2=sp.integrate(eq1, x)+c2

print(eq2/(E*I))