try:
    fin = open("input.txt","r")
    lines = fin.readlines()
    if lines==[]:
        print("File is Empty")
    else:
        print("Total Number of lines: ",len(lines))
    fin.close()
except FileNotFoundError:
    print("File Doesn't exist")