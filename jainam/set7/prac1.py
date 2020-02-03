class AddressBook:
	book=[]
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
    
	@classmethod
	def createUser(cls):
		name = input("Enter Name: ")
		contact = input("Enter Contact: ")
		cls.book.append(AddressBook(name,contact))
		
	@classmethod
	def display(cls):
		for user in cls.book:
			print(user.name + "\t\t" + user.contact)

	@classmethod
	def updateContact(cls):
		name = input("Enter Name: ")
		for user in cls.book:
			if user.getName()==name:
				user.setContact(input("Enter Contact: "))
				return;
		print("User not Found")

def switch(c):
    fun={'1':AddressBook.createUser,'2':AddressBook.display,'3':AddressBook.updateContact}
    return fun[c]

def menu():
    print("1) Enter New User\n2) Display Address Book\n3) Update Contact of User")

while True:
    menu()
    c = input("Enter choice: ")
    if c>'0' and c<'4':
        switch(c)()
    else:
        break
