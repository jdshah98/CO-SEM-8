class Bird:
	def __init__(self,bird_type):
		self.type = bird_type
		print(self.type,"is ready")
	
	def fly(self):
		if self.hasWings:
			print(self.type,"can fly")
		else:
			print(self.type,"can't fly")

class Parrot(Bird):
	def __init__(self):
		super().__init__("Parrot")
		self.hasWings=True

class Penguin(Bird):
	def __init__(self):
		super().__init__("Penguin")
		self.hasWings=False


def flying_test(bird):
    bird.fly()

bird1 = Parrot()
bird2 = Penguin()
flying_test(bird1)
flying_test(bird2)
