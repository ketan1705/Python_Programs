'''def f(n,m):
    if(m==0):
        return 1
    elif(m==1):
        return n
    else:
        return n*f(n,m-1)
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
t=f(n,m)
print(t)
'''
# Wap to find addition  of two number using recursion
'''
def add(n,m):
    if(m==0):
        return n
    else:
        return 1+add(n,m-1)
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
t=add(n,m)
print(t)
'''
# Wap to find multiplication of two number using recursion

def mul(n,m):
    if(m==1):
        return n
    else:
        return n+mul(n,m-1)
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
t=mul(n,m)
print(t)