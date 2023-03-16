def scretInfo(text,name):
    text.islower()
    t = 0
    length = len(text)
    i = 0
    print(length)
    for i in range(length):
        if(t==len(name)):
            break
        if(text[i] == name[t]):
            t += 1
        else:
            t = 0
            
    if(t<len(name)):
        return -1
    else:
        return(i-t)
    return

def main():
    text =  str(input())

    name = str(input())

    result = scretInfo(text,name)
    print(result)

if __name__== "__main__":
    main()