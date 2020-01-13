def Sum(list):
    sum=0
    for i in list:
        sum+=float(i)
    return sum

list = input("Enter list of numbers seperated by comma: ").split(",")
print("Sum: ",Sum(list))