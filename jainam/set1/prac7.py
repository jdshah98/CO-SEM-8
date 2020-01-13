a = int(input("Enter a: "))
b = int(input("Enter b: "))
sum=0
for i in range(a,b):
    if i%3==0:
        sum+=i
print("Sum: ",sum)