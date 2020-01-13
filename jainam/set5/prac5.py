l = ['p','q']
n=5
out=[]
for i in range(1,n+1):
    for j in l:
        out.append(j+str(i))
print(out)