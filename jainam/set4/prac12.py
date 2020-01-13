try:
    fin = open("prac12.txt","r")
    lines = fin.readlines()
    fin.close()
    if lines==[]:
        print("File is Empty")
    else:
        line_no=int(input("Enter Line No of File to read: "))
        if line_no<=0 or line_no>len(lines):
            print("File Length Exceeded")
        else:
            print(lines[line_no-1])
except FileNotFoundError:
    print("File Doesn't exist")