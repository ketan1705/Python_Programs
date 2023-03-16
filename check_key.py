n=input("Enter the key:")
d={'a':1,'b':2,'c':3,'d':4}
if n in d:
    print("key is exist in dictionary")
else:
    print("key is not exist in dictionary")


#for making user defined
'''
d={int(x):int(z) for x in input("Enter the key: ").split() for z in input("Enter the value: ").split()}
'''

