a=int(input("Enter the number: "))
sum=0
temp=a
c=len(str(a))
while temp>0:
    r=temp%10
    sum=sum+(r**c)
    temp=temp//10
if a==sum:
    print(a,'is a Armstrong number')
else:
    print(a,'is not a Armstrong number')
    
  