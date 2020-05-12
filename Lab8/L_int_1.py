n=100
deltax=0.8/n
X=[0]*(n+1)

def func(x):
    f=0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
    return f

for i in range(n+1):
    X[i]=deltax*i

Area=0.0

for i in range(n):
    funx=func(X[i])
    funcx1=func(X[i+1])
    Area+=0.5*(funcx1+funx)*deltax

print(Area)