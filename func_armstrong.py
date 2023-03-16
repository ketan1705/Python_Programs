# Write a function to check number is armstrong or not

def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        r=temp%10
        sum=sum + (r**3)
        temp=temp//10
    if(n==sum):
        return (n,"is armstrong number")
    else:
        return (n,"is not armstrong number")

n=int(input("Enter the number"))
t=armstrong(n)
print(t)