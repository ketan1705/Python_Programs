'''n=int(input("Enter the limit: "))
for i in range(n+1):
    print(i)'''
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')'''

'''
n=int(input("Enter the number: "))
sum=0
for i in range(n+1):
    sum=sum+i
else:
    print(sum)'''

'''
n=int(input("Enter the number: "))
for i in range(1,11):
    print(n*i)
'''
'''
list1=[12,15,32,42,55,75,122,132,150,180,200]
for item in list1:
    if item>150:
        break
    elif item %5 == 0:
        print(item)
    '''
'''
n=int(input("Enter the number: "))
count=0
while n!=0:
    n=n//10
    count=count+1
print(count)
'''

'''
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print(' ')'''

'''
list1=[10,20,30,40,50]
for i in (list(reversed(list1))):
    print(i)'''
'''
list1=[10,20,30,40,50]
start=len(list1)-1
stop=-1
step=-1
for i in range(start,stop,step):
    print(list1[i])'''
'''
for i in range(-10,0,1):
    print(i)
'''

for i in range(5):
    print(i)
else:
    print("DONE")


    