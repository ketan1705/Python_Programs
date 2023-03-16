# Write a fucntion to check number is prime or not

'''
def prime(n):
    x=n//2
    while(x>1):
        if n%x==0:
            return (n,"is not prime")
            break
        x=x-1
    else:
        return (n,"is a prime number")
n=int(input("Enter the number:"))
t=prime(n)
print(t)'''

def prime(n):
    c=0
    for i in range(2,n//2+1):
        if(n%i==0):
            c=c+1
            break
    return c
n=int(input("Enter the number:"))
t=prime(n)
if(t==0):
    print("Number is prime")
else:
    print('Number is not prime number')