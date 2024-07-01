favorite_places = {
	'Fatima': ['Wasser'], 
	'Aspernig': ['BT'], 
	'Alexander': ['Zuhause', 'Bett', 'Computer']
	}

for name, places in favorite_places.items():
	if len(places) == 1:
		print(f"{name.title()}'s favorite place is: \n\t{places[0]}")
	else:
		print(f"{name.title()}'s favorite places are:")
		for place in places:
			print(f'\t{place.title()}')
			
