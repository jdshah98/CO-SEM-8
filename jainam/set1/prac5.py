base = float(input("Enter base number: "))
power = int(input("Enter power: "))
ans=1
while power>0:
    ans*=base
    power-=1
print("Answer: ",ans)