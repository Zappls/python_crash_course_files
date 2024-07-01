from restaurant import Restaurant

class Flavors:
	def __init__(self):
		"""Initiating a empty list to hold all the flavors to be added later."""
		self.flavors = []
		
	def add_flavors(self, *flavors):
		"""Adds flavors to the end of the list"""
		self.flavors.extend(flavors)

	def display_flavors(self):
		"""Prints a alphabetical list of flavors."""
		print(sorted(self.flavors))

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		"""Initializing parent class."""
		super().__init__(restaurant_name, cuisine_type)
		"""Initializing child class with flavors argument."""
		self.flavors = Flavors()



my_stand = IceCreamStand('NicesIce', 'Ice Cream')
my_stand.flavors.add_flavors('Vanilla', 'Choco', 'Mint', 'Peanut Butter')
my_stand.flavors.display_flavors()