n=int(input("enter the limit: "))
for i in range(n+1):
    for j in range(i):
        print(j+1,end=" ")
    for j in range(i,1,-1):
        print(j-1,end=" ")
    print()    
    
    