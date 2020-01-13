class Bank:
    no=0
    def __init__(self,name,contact,amount):
        self.name = name
        self.contact = contact
        self.amount = amount
        self.accno = '427' + str(no+1).rjust(4,0)
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getContact(self):
        return self.contact
    
    def setContact(self,contact):
        self.contact = contact

    def getAmount(self):
        return self.amount
    
    def setAmount(self,amount):
        self.amount = amount
    
    def getAccountNo(self):
        return self.accno
    
def createUser(bank):
    name = input("Enter Name: ")
    contact = input("Enter Contact: ")
    amount = input("Enter Amount: ")
    bank.append(Bank(name,contact,amount))
    
def display(bank):
    for user in bank:
        print(user.name + "\t\t" + user.contact)

def updateContact(bank):
    name = input("Enter Name: ")
    for user in bank:
        if user.getName()==name:
            user.setContact(input("Enter Contact: "))
            return;
    print("User not Found")

def switch(c):
    fun={'1':createUser,'2':display,'3':updateContact}
    return fun[c]

def menu():
    print("1) Enter New User\n2) Display Address bank\n3) Update Contact of User")

bank=[]
while True:
    menu()
    c = input("Enter choice: ")
    if c>'0' and c<'4':
        switch(c)(bank)
    else:
        break