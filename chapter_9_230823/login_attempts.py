class User:
	def __init__(self, first, last, age, status):
		self.first = first
		self.last = last
		self.age = age
		self.status = status
		self.login_attemps = 0

	def describe_user(self):
		print(f"The user, {self.first} {self.last} "
			f"is {self.age} old and {self.status}.")

	def greet_user(self):
		print(f"Welcome back, {self.first} {self.last}!")

	def increment_login_attempts(self):
		"""Increments login_attempts by 1."""
		self.login_attemps += 1

	def reset_login_attempts(self):
		"""Resets login_attempts to 0."""
		self.login_attemps = 0

mama = User('Maria', 'Wolfger', 61, 'offline')
me = User('Alexander', 'Wolfger', 29, 'terminally online')

me.describe_user()
me.greet_user()

me.increment_login_attempts()
print(me.login_attemps)
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attemps)

me.reset_login_attempts()
print(me.login_attemps)

