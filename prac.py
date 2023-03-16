'''
import math
import os
import random
import re
import sys

def fizzBuzz(n):
    for i in range(1,n):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
'''
'''
i=45
while(True):
    if i+1<55:
        i=i+1
        continue
    print(i+1,end=" ")
    if(i==85):
        break
    i=i+1'''
'''
print("enter your number")
anik=int(input())
print("enter your second number")
ketan=int(input())
print("select your sign")
sign=input()
if sign=='+' and anik==45 and ketan==44:
  print("30")
elif sign=='+':
  print(anik+ketan)
else:
  print("invalid")

'''
'''
a=[1,5,6,1,7,9]
print(a[:-2])

b=[4,5,6,7]
b.append(a)
print(b)

print(a+b)
'''
'''
del a[2]
del a[:2]
print(a)'''
'''
square={1:1,3:9,5:25,7:49,9:81}
for i in square:
    print(square[i])'''
'''
students={'name':'Mohan','age':20,'course':['bca','mca']}
for key,values in students.items():
    print(key,values)'''


'''n=list((x for x in input("Enter the numbers")))
n.sort()
y=max.n
print(y)
'''
'''def employee(name,salary=9000):
    return (name,salary)
n=input("Enter the name:")
m=int(input("Enter the salary:"))
x=employee(n,m)
print(x)'''
'''
f=open("ken.txt",'r')
counter=0
for i in f:
    counter=counter+1
print(counter)'''


'''with open("abc.txt",'w') as f:
    f.write("This is gla university")
    with open("abc.txt",'r') as a:
        with open("abcd.txt",'w') as n:
            a.seek(10)
            b=a.read()
            c=b[::-1]
            n.write(c)
'''
'''import turtle 
colors = ['red','green','yellow','purple','blue']
t = turtle.pen()
t.speed(10)
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%5])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
turtle.done()'''




class test:
    var = 'aa'
    def fun(self,str):
        print('something')
        self.var= test.var+str+str










