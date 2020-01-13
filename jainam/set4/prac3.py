try:
    fin = open("input.txt","r")
    lines = fin.readlines()
    fin.close();
    if lines==[]:
        print("File is Empty")
    else:
        fupper = open("prac3_upper.txt","w")
        flower = open("prac3_lower.txt","w")
        print("File In Upper Case:")
        for i in lines:
            fupper.write(i.upper())
            print(i.upper(), end='')
        print("\n\nFile In Lower Case:")
        for i in lines:
            flower.write(i.lower())
            print(i.lower(), end='')
        fupper.close()
        flower.close()
except FileNotFoundError:
    print("File Doesn't exist")