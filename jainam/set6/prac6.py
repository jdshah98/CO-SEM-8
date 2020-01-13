l = ['Johnny','Russell','Scarlett','Russell','Johnny','Mark']
d = dict.fromkeys(l,0)
for i in l:
    d[i]+=1
print(d)