print("Let me help you order a pizza.\n")
print("What size would you like?\na. small(200)\tb. medium(350)\tc.large(500)")
c = input("Please enter a or b or c: ")
if c=='a':
    print("Ok, small, that is 200 Rs. each ")
    count = int(input("How many would you like? "))
    print("Your Total is Rs.",count*200)
elif c=='b':
    print("Ok, medium, that is 350 Rs. each ")
    count = int(input("How many would you like? "))
    print("Your Total is Rs.",count*350)
elif c=='c':
    print("Ok, large, that is 500 Rs. each ")
    count = int(input("How many would you like? "))
    print("Your Total is Rs.",count*500)
else:
    print("Choice unavailable")