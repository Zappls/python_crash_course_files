from users import Users

class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

class Admin(Users):
	"""Initiating parent and child class."""
	def __init__(self, first, last, age, status):
		self.first = first
		self.last = last
		self.age = age
		self.status = status
		super().__init__(first, last, age, status)
		self.privileges = Privileges(['can add post', 'can delete post', 'can ban user',
		'can sticky post'])

	

"""alex = Admin('Alexander', 'Wolfger', 29, 'terminally online')
alex.privileges.show_privileges()



new_admin = Admin('Michael', 'Müller', 123, 'offline')
new_admin.privileges.show_privileges()"""