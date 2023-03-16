'''a=open("ken.txt",'r')
b=open("raj.txt",'w')
for i in a:
    b.write(i)'''
'''
n=input("Enter file name")
f=open(n+".txt",'r')
for i in f:
    for j in i:
        if(j.isdigit()):
            print(j)
'''
# find the length of the file
'''n=input("Enter file name")
f=open(n+".txt",'r')
a=0
for i in f:
    w=i.split()
    a=a+len(w)
print(a)
'''
# to read the line from the file
'''
a=input("Enter the file name")
f = open(a+".txt","r")
n = 0
for i in f:
    n = n + 1
print("Total Lines:",n)'''
# Write the name in the file and the read and print on the screen
'''with open("name.txt",'w') as namefile:
    namefile.write("Name: Ketan\nRoll NO: 15")
with open('name.txt','r') as name:
        text=name.read()
        print(text)
print("DOne")
'''
# Make the file of user name and store the data in it

'''
with open("name.txt",'w') as namefile:
    namefile.write("Ketan\nraj\nsparsh\nharsh\nanik")
with open('message.txt','w') as messagefile:
    messagefile.write("Hi how are you")
with open('name.txt','r') as name:
    with open('message.txt','r') as me
    ssage:
        text=message.read()
        for n in name:
            mail="Dear Mr. "+n+text
            with open(n.strip()+'.txt','w') as mailfile:
                mailfile.write(mail)
print("DOne")'''

# After the create the file some extra data
'''
q = input("Enter the file name: ")
f = open(q + ".txt","a")
s = input("Enter the string: ")
f.write("\n" + s)
f.close()
f = open(q + ".txt","r")
n = 0
for i in f:
    n = n + 1
print("Total lines: ",n)'''

# Count the string from the file
'''q = input("Enter the file name: ")
f = open(q + ".txt","r")
s = input("Enter the string: ")
n = 0
for i in f:
    if(s in i):
        n = n + 1
print("Total lines: ",n)

'''
'''
a = input("Enter the file name:")
f = open(a+".txt","r")
q = f.read()
print(q)
f.close()'''

'''
a = input("Enter the file name:")
f = open(a+".txt","r")
q = f.read()
for i in q:
    if(i.isdigit()):
        print(i)
f.close()'''

#Copy the data from file to the new file

'''n = input("Enter the file name:")
with open(n + ".txt","r") as f:
    with open("new.txt","w") as t:
        t.write(f.read())
print("File copied successfully")'''
