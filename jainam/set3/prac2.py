def Multiply(list):
    prod=1
    for i in list:
        prod*=float(i)
    return prod

list = input("Enter list of numbers seperated by comma: ").split(",")
print("Product: ",Multiply(list))