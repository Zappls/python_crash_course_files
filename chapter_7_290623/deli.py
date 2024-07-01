sandwich_orders = ['Tomato-Mozzarella sandwich', 'BLT-sandwich', 'Pulled Pork-sandwich']

finished_sandwiches = []

while sandwich_orders:
	popped_sandwich = sandwich_orders.pop()
	print(f"I made your {popped_sandwich}!")
	finished_sandwiches.append(popped_sandwich)

print(f"\nThe sandwiches that were made are:")
for sandwich in finished_sandwiches:
	print(sandwich)