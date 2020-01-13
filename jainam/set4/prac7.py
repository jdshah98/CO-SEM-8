try:
    fin = open("input.txt","r")
    lines = fin.readlines()
    fin.close()
    if lines==[]:
        print("File is Empty")
    else:
        content = ''.join(lines)
        print(content[::-1])
except FileNotFoundError:
    print("File Doesn't exist")