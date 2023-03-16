n=(input("Enter the string: "))
rev_str=reversed(n)
if list(rev_str)==list(n):
    print("String is pallindrom")
else:
    print("String is not pallindrom")