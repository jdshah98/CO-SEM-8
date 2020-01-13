array = [int(i) for i in input("Enter numbers seperated by space: ").split(" ")]
sum=0
for i in array:
    sum+=i
print("Sum: ",sum)