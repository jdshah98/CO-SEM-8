def prime(n):
    if n<2:
       return False 
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    return False

n = int(input("Enter Number: "))
if prime(n):
    print(n," is prime")
else:
    print(n," is not prime: ")