l=int(input("Enter lower limit"))
u=int(input("Enter the upper limit"))

for i in range(l,u+1):
    if(i>1):
        for j in range(2,(i//2)):
            if i % j == 0:
                break
        else:
            print(i)