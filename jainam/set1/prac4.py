import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b*b - 4*a*c
if d<0:
    print("Roots are complex")
elif d==0:
    x = (-b)/(2*a)
    print("Roots are equal")
    print("x: ",x)
else:
    x1 = (-(b) + math.sqrt(d))/(2*a)
    x2 = (-(b) - math.sqrt(d))/(2*a)
    print("Roots are Distinct and Real")
    print("x1: ",x1)
    print("x2: ",x2)