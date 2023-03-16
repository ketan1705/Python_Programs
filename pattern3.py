n=int(input("enter the limit: "))
for i in range(n+1):
    for m in range(n-i):
        print(" ",end=" ")
    for j in range(i):
    
        print(j+1,end=" ")
    for k in range(i,1,-1):
        print(k-1,end=" ")
    print()
    