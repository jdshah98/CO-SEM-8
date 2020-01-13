try:
    fin = open("prac11.txt","r")
    lines = fin.readlines()
    fin.close()
    if lines==[]:
        print("File is Empty")
    else:
        sum=0
        for i in lines:
            sum+=int(i)
        print("Sum:",sum)
except FileNotFoundError:
    print("File Doesn't exist")