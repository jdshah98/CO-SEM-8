a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a>b:
    if a>c:
        print(a," is greatest")
    else:
        print(c," is greatest")
else:
    if b>c:
        print(b," is greatest")
    else:
        print(c," is greatest")