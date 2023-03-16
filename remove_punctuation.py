
punctuation="!@#$%^&*()_{}[].><,/?`~"
str1=input("Enter the string: ")
notpunctuation=''
for char in str1:
    if char not in punctuation:
        notpunctuation=notpunctuation+char
print(notpunctuation)