class Users:
	def __init__(self, first, last, age, status):
		self.first = first
		self.last = last
		self.age = age
		self.status = status

	def describe_user(self):
		print(f"The user, {self.first} {self.last} "
			f"is {self.age} old and {self.status}.")

	def greet_user(self):
		print(f"Welcome back, {self.first} {self.last}!")

"""mama = Users('Maria', 'Wolfger', 61, 'offline')
me = Users('Alexander', 'Wolfger', 29, 'terminally online')"""



