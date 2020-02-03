import random, re

class Bank:
	no=0
	bank={}
	def __init__(self,name,contact,amount):
		self.name = name
		self.contact = contact
		self.amount = amount
		self.accno = '427' + str(Bank.no+1).rjust(4,'0')
		self.pin = str(random.randint(1,9999)).rjust(4,'0')

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
	
	def displayAccount(self):
		print("Your Account Created Successfully")
		print("Your Account No: ",self.accno)
		print("Your Pin No: ",self.pin)

	def deposit(self):
		amt = int(input("Enter amount: "))
		self.setAmount(int(self.getAmount())+amt)
		print("Your Account Balance: ",self.amount)

	def withdraw(self):
		amt = int(input("Enter amount: "))
		if int(self.getAmount())-1000<amt:
			print("You cannot withdraw only upto ",int(self.getAmount())-1000)
		else:
			self.setAmount(int(self.getAmount())-amt)
			print("Your Account Balance: ",self.amount)		

	@classmethod 
	def createAccount(cls):
		name = input("Enter Name: ")
		contact = input("Enter Contact: ")
		amount = input("Enter Amount: ")
		user = Bank(name,contact,amount)
		cls.bank[user.accno] = user
		user.displayAccount()

	@classmethod
	def operateAccount(cls):
		accno = input("Enter Account No: ")
		if cls.bank.get(accno) is not None:
			user = cls.bank.get(accno)
			pin = input("Enter Pin: ")
			if user.pin==pin:
				while True:
					print("1) Deposit\n2) Withdraw")
					c = int(input("Enter choice: "))
					if c==1:
						user.deposit()
					elif c==2:
						user.withdraw()
					else:
						break
			else:
				print("Incorrect Pin")
		else:
			print("Account No doesn't exist")

	@classmethod
	def searchAccount(cls):
		accno = input("Enter account No: ")
		acc_regex = re.compile(r'427\d{4}')
		if acc_regex.search(accno) is not None:
			if acc_regex.search(accno).group()==accno:
				print("Valid")
			else:
				print("invalid")
		else:
			print("invalid")

while True:
	print("1) Create New Account\n2) Operate Existing Account\n3) Search a valid Account No")
	c = int(input("Enter choice: "))
	if c==1:
		Bank.createAccount()
	elif c==2:
		Bank.operateAccount()
	elif c==3:
		Bank.searchAccount()
	else:
		break
