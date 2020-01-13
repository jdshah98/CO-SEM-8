import os

filename=input("Enter Filename: ")
if os.path.exists(filename):
    print("Exists")
    if os.path.isfile(filename):
        print(filename,"is Regular file")
        print("Size: ",os.stat(filename).st_size)
    else:
        print(filename,"is Directory File")
else:
    print(filename,"doesn't exists")