l = input("Enter comma seperated list of numbers: ").split(",")
for i in l:
    if int(i)%2==0:
        print(i)