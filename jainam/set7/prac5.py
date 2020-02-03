class EMP:
	def __init__(self,id,name,salary):
		self.id = id
		self.name = name
		self.salary = salary
	
	def getName(self):
		return self.name
	
	def getId(self):
		return self.id
	
	def getSalary(self):
		return self.salary

class Person(EMP):
	id = 0
	def __init__(self,name,salary):
		super().__init__(Person.id+1,name,salary)
		Person.id = Person.id + 1
	
	def display(self):
		print("Id: ",self.getName())
		print("Name: ",self.getId())
		print("Salary: ",self.getSalary())

p1 = Person("jainam",20000)
p1.display()
