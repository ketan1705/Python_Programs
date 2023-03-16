string1=input("Enter the string: ")
n=len(string1)
if n>2:
    string2=string1[:3] + string1[-2:]
    print(string2)
else: 
    print("String is empty")