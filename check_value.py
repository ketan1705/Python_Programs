d={(x):(z) for x in input("Enter the key: ").split() for z in input("Enter the value: ").split()}

n=input("Enter the key to search: ")
for i in d:
    if i==n:
        print('Key is found.\nValue at that key is',d[i])
        break;
else:
    print('Not found')