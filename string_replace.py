
string1=input("Enter the string: ")
char = string1[0]
string1 = string1.replace(char,'#')
string1 = char + string1[1:]
print(string1)
        