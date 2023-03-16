
vowels='aeiouAEIOU'
string1=input("Enter the string: ")
count={}.fromkeys(vowels,0)
for i in vowels:
    for j in string1:
        if(i==j):
            count[i]+=1
print(count)