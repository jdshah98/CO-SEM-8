class Student:
	id=0
	l = {}
	def __init__(self,name,contact):
		Student.id = Student.id+1
		self.id = Student.id
		self.name = name
		self.contact = contact
		Student.l[Student.id] = self
	
	def getId(self):
		return self.id

	def getName(self):
		return self.name
	
	def setName(self,name):
		self.name = name

	def getContact(self):
		return self.contact
	
	def setContact(self,contact):
		self.contact = contact

	@classmethod
	def display(cls):
		print("ID\t\tName\t\tContact")
		for i in range(1,cls.id+1):
			print(cls.l[i].id,cls.l[i].name,cls.l[i].contact,sep='\t\t')

s1 = Student('jainam','8469368554')
s2 = Student('smit','7990501583')
s3 = Student('alaukik','7990643640')
Student.display()
