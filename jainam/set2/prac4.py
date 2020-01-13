c = int(input("1)Number Pattern\n2)Symbol Pattern\nEnter Choice: "))
if c==1:
    n = int(input("Enter number of lines: "))
    k=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(k, end=" ")
            k+=1
        print()
elif c==2:
    n = int(input("Enter number of lines: "))
    for i in range(1,n+1):
        for j in  range(n,i,-1):
            print(" ",end=" ")
        for j in range(1,i+1):
            if i%2==0:
                print("!",end=" ")
            else:
                print("#",end=" ")
        print()
else:
    print("Wrong Choice")