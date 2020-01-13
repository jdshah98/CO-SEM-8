charArray = [i for i in input("Enter String: ")]
temp = [(ord(i),i) for i in charArray]
for i in sorted(temp):
    print(i[1], end=', ')