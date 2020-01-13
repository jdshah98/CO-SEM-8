try:
    fin = open("input1.txt","r")
    lines1 = fin.readlines()
    fin.close()
    fin = open("input2.txt","r")
    lines2 = fin.readlines()
    fin.close()
    if lines1==[]:
        print("File1 is Empty")
    elif lines2==[]:
        print("File2 is Empty")
    else:
        content=''.join(lines1) + "\n" + ''.join(lines2)
        fout = open("prac6.txt","w")
        fout.write(content)
        print("done")
        fout.close()
except FileNotFoundError:
    print("File Doesn't exist")