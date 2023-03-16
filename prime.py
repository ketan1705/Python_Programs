y=int(input("enter the value"))

x=y//2
while(x>1):
    if y%x==0:
        print(y,'has factor',x,"not prime")
        break
    x=x-1
else:
    print(y,'is a prime no')
    
    
  #PRIME USING flag variable

'''y=int(input("enter the value"))
x=y//2
flag=0
while(x>1):
    if y%x==0:
        flag=1
        break
    x=x-1        
if(flag == 1):
        print(y,'has factor',x,"not prime")
else:
        print(y,"is a prime number")'''