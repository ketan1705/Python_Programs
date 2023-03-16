
'''
l1=[5,4,1,3,14,]
l2=[9,8,46,452,15,15]
l3=[]
l3.extend(l1)
l3.extend(l2)
print(l3)
'''
'''
l1=[54,44,27,79,91,41]
print("original list",l1)
l1.pop(4)
l1.insert(2,11)
print("list after adding element at index at 2",l1)
l1[len(l1):]=[11]
print("list after adding element at last",l1)'''
'''
l1=[11,45,8,23,14,12,78,45,89]
l=len(l1)
size=int(l//3)
start=0
end=size
for i in range(1,4):
    index=slice(start,end,1)
    result=l1[index]
    print(result)
    print(list(reversed(result)))
    start=end
    if i!=2:
        end=end+size
    else:
        end=end+l-size'''
'''
list1=(input("Enter the list: "))
list2=list1.split()
list3=(input("Enter the list: "))
list4=list3.split()
print(list2)
print(list4)
result=zip(list2,list4)
result1=set(result)
print(result1)
'''
'''
s1={65,78,9,4,5,4,265,151,1}
s2={15,89,41,7,1,61}
intersection1=s1.intersection(s2)
print(intersection1)
for i in intersection1:
    s1.remove(i)
print(s1)'''
'''
s1 = {57, 83, 29}
s2 = {67, 73, 43, 48, 83, 57, 29}

if(s1.issubset(s2)):
    s1.clear()
    print(s1)
elif(s2.issubset(s1)):
    s2.clear()
    print(s2)'''
