t=1,2,4,5
t+=t[:2] + tuple([3]) + t[2:]
print(t)