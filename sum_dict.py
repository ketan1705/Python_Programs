d={(x):int(z) for x in input("Enter the key: ").split() for z in input("Enter the value: ").split()}
print(d)
#d1={'a':1,'b':2,'c':3,'d':4}
sum=0
for i in d.values():
    sum=sum+i
print(sum)
