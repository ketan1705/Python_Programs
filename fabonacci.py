n=int(input("Enter the limit: "))
x=0
y=1
print(x)

while n>1:
    print(y)
    s=x+y
    x=y
    y=s
    n=n-1