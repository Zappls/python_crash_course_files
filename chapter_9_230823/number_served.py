class Restaurant:
	"""Model for a restaurant that describes it and tells you when it's open."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints info about the restaurant."""
		print(f"{self.restaurant_name} is a {self.cuisine_type} cuisine restaurant.")

	def open_restaurant(self):
		"""Prints msg indicating that the restaurant ist open."""
		print(f"The restaurant {self.restaurant_name} is open.")

	def customers_served(self):
		"""Print the number of customers served."""
		print(f"{self.restaurant_name} has served {self.number_served}"
			f" customers today.")
	def set_number_served(self, number):
		if number >= 0:
			self.number_served = number
		else:
			print("You can't serve negative amounts of customers.")

	def increment_number_served(self, number):
		if number >= 0:
			self.number_served += number
		else:
			print("You can't unserve already served customers.")

restaurant = Restaurant('McD', 'american')
restaurant.customers_served()

restaurant.number_served = 5
restaurant.customers_served()

restaurant.set_number_served(27)
restaurant.customers_served()

restaurant.increment_number_served(393)
restaurant.customers_served()