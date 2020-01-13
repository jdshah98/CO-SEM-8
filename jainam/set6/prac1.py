l = input().split(",")
for i in range(0,len(l),2):
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp
print(l)