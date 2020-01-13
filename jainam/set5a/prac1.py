charArray = input("Enter String: ").split()
print("Characters encoded in utf-8")
for i in charArray:
    print(i.encode())
print("résumé".encode("utf-8"))