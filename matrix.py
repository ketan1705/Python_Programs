# matrix 
'''r,c = input().split()
r,c = int(r),int(c)
k=1
for i in  range(r):
    for j in range(c):
        if j == (c-1):
            print(k,end="")
            k=k+1
        else:
            print(k,end=" ")
            k=k+1
    print()'''

#only diagonal print
'''r,c = input().split()
r,c = int(r),int(c)
k=1
for i in  range(r):
    for j in range(c):
        if j == i:
            print(k,end=" ")
            k=k+1
        else:
            print(k,end=" ")
            k=k+1
    print()'''

r,c = input().split()
r,c = int(r),int(c)
k=1
for i in  range(r):
    for j in range(c):
        if j == (c-1):
            print(k,end="")
            k=k+1
        else:
            print(k,end=" ")
            k=k+1
    print()