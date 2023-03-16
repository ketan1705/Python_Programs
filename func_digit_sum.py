# Write a program to sum of digit of number

def sumofdigit(n):
    rev=0
    temp=n
    while(temp>0):
        digit=temp%10
        rev=rev + digit
        temp=temp//10
    return rev
        
n=int(input("Enter the number:"))
t=sumofdigit(n)
print(t)