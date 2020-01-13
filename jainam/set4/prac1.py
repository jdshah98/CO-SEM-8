a = input("Enter a: ")
b = input("Enter b: ")
fout = open("prac1.txt","w")
fout.write(a + "\n")
fout.write(b)
fout.close()
fin = open("prac1.txt","r")
for x in fin:
    print(x)