class Restaurant:
	"""Model for a restaurant that describes it and tells you when it's open."""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		"""Prints info about the restaurant."""
		print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
	def open_restaurant(self):
		"""Prints msg indicating that the restaurant ist open."""
		print(f"The restaurant {self.restaurant_name} is open.")

#florianihof = Restaurant('Florianihof', 'Altwienerküche')

#florianihof.describe_restaurant()
#florianihof.open_restaurant()

#tseng = Restaurant('Tseng', 'Asiatisch')

#tseng.describe_restaurant
