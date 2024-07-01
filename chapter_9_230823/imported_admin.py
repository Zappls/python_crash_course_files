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

class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

class Admin(Users):
	"""Initiating parent and child class."""
	def __init__(self, first, last, age, status):
		super().__init__(first, last, age, status)
		self.privileges = Privileges(['can add post', 'can delete post', 'can ban user',
		'can sticky post'])

