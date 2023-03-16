sub1=float(input("Enter the 1 subjects marks: "))
sub2=float(input("Enter the 2 subjects marks: "))
sub3=float(input("Enter the 3 subjects marks: "))
sub4=float(input("Enter the 4 subjects marks: "))
sub5=float(input("Enter the 5 subjects marks: "))

per=(sub1+sub2+sub3+sub4+sub5)/5
print(per)

if (per>=91 and per<=100):
    print("Grade is A+")
elif (per>=81 and per<=90):
    print("Grade is A")
elif(per>=71 and per<=80):
    print("Grade is B+")
elif(per>=61 and per<=70):
    print("Grade is B")
elif(per>=51 and per<=60):
    print("Grade is C+")
elif(per>=41 and per<=50):
    print("Grade is C")
else:
    print("Grade is F")