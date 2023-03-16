def outer(a,b):
    c=inner(a,b)+5
    return c
def inner(e,f):
    d=e+f
    return d
n=int(input("Enter the first number"))
m=int(input("Enter the second number"))
x=outer(n,m)
print(x)