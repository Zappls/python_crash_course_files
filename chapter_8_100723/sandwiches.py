def make_sandwich(*ingredients):
	print(f"\nMaking a sandwich with the following ingredients:")
	for ingredient in ingredients:
		print(f"\t- {ingredient.title()}")

#make_sandwich('Tomato', 'Bacon', 'Cheese', 'Mayo')
#make_sandwich('Pulled Pork', 'Mayo')
#make_sandwich('Garlic butter', 'Steak', 'Cheddar')