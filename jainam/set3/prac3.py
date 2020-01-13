def factorial(n):
    if n==0 or n==1: 
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter Number: "))
if n<0:
    print("Enter Non-negative number")
else:
    print("Factorial: ",factorial(n))