def removeDuplicates(l):
    return list(dict.fromkeys(l))
l = input("Enter some comma seperated elements: ").split(",")
print(removeDuplicates(l))