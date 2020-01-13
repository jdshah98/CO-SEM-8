list = input("Enter List of numbers seperated by comma: ").split(",")
even=[]
for i in list:
    if int(float(i))%2==0:
        even.append(int(i))
print(even)