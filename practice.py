'''n=int(input("enter the number")) 

s=0
while(n!=0):
    a=n%10
    s=s+a
    n=n//10
print(s)
'''

'''
1) write a python program to find sum all items in a dictionary
2) Write  program in python that asks the user to input username and password 
from five users. The data should be stored such that the username in non editable
while the password is editable.
3) Python program to check whether a string is
pallindrom or not. 
'''
'''
n=[[x,int(y) for x range(1) for y in range(1)] for m in range[input("Enter the  limit: ")]]
print(n)
a=y.min(y)
b=index(a)
c=b.(index(x)-1)
print(c)'''
'''
def fun():
    """function to add two values"""
    x=10
    print("value inside function:",x)'''
'''
fun.__doc__
s=fun(3,4)
print(s)'''
'''x=20
fun()
print("Value outside function:",x)
'''

'''
1) python program to remove punctuations from a string
2) python program to sort words in alphabetic order.
3) python program to count the number of each vowel
'''
''' 
1)   Write a python program to get a string made of the first
    3 and the last 2 chars from a given a string.If the string length is length
    than 2, return instead of the empty string
 Ex: input: university
    output: unity

2)  Write a python program to get a string from a given string where all occurence 
of its first char have been changed to '#' , except the first char itself.
Ex : Input: connection
    output: cone#tion
 '''


# Wap To program to find all even number between given range using lambda function
# Wap to find area of triangle of a right angle triangle using lambda function

'''n=int(input("Enter the range:"))
print(list(filter(lambda a:(a%2==0),range(0,n))))
'''
'''
Area = lambda b,h:0.5*b*h
b=int(input("Enter the base:"))
h=int(input("Enter the height:"))
print(Area(b,h))'''

# Wap to count digit,words and special symbol in a file,

a='!@#$%^&*()_~`"";,.{}[]\/?><'
n=input("Enter the file name: ")
f=open(n+".txt",'r')
alphabet=digit=special=0
for i in f:
    for j in i:
        if (j.isdigit()):
            digit+=1
        elif(j.isalpha()):
            alphabet+=1
        else:
            special+=1
print("Total digit:",digit)
print("Total alphabet:",alphabet)
print("Total special:",special)