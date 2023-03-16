def fact(n):
    f=1
    if(n==0):
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
    return f
 
n=int(input("Enter the number:"))
factorial=fact(n)
print("Factorial of",n,"=",factorial)