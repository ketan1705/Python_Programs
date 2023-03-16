# Write a fucntion to check number is pallindrom or not


def pallindrom(n):
    rev=0
    temp=n
    while(temp>0):
        digit=temp%10
        rev=rev*10 + digit
        temp=temp//10
    if(n==rev):
        return (n,"is a pallindrom number")
    else:
        return (n,"is not a pallindrom number")

n=int(input("Enter the number"))
t=pallindrom(n)
print(t)