class Addressbook:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getContact(self):
        return self.contact
    
    def setContact(self,contact):
        self.contact = contact
    
def createUser(book):
    name = input("Enter Name: ")
    contact = input("Enter Contact: ")
    book.append(Addressbook(name,contact))
    
def display(book):
    for user in book:
        print(user.name + "\t\t" + user.contact)

def updateContact(book):
    name = input("Enter Name: ")
    for user in book:
        if user.getName()==name:
            user.setContact(input("Enter Contact: "))
            return;
    print("User not Found")

def switch(c):
    fun={'1':createUser,'2':display,'3':updateContact}
    return fun[c]

def menu():
    print("1) Enter New User\n2) Display Address Book\n3) Update Contact of User")

book=[]
while True:
    menu()
    c = input("Enter choice: ")
    if c>'0' and c<'4':
        switch(c)(book)
    else:
        break