try:
    fin = open("input.txt","r")
    lines = fin.readlines()
    if lines==[]:
        print("File is Empty")
    else:
        content = ''.join(lines).lower()
        d = dict().fromkeys(content,0)
        for i in d.keys():
            d[i]=content.count(i)
        print(d)
    fin.close()
except FileNotFoundError:
    print("File Doesn't exist")