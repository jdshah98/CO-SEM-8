def getKey(val):
    return val[1]
l= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l.sort(key=getKey)
print(l)