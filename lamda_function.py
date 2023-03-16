#lambda function

#using of map function in lambda

'''li = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda a:a*a,li)))
'''
'''
li=[1,2,3,4,5,6,7]
def square(a):
    return a*a
print(list(map(square,li)))'''

'''l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(list(map(lambda x,y:x+y,l1,l2)))
'''

#using of filter function in lambda
'''
print(list(filter(lambda a:a%2!=0,range(1,50))))'''

# Program using map 
 
def fahrenheit(T):
    return ((float(9/5))*T + 32)
temp=[36.5,37,37.5,39]
F=map(fahrenheit,temp)
print(list(F))