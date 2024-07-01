cities = {
	'Klagenfurt': {
		'country': 'austria',
		'population': '100,000',
		'fact': 'my birthplace',
	},
	'Vienna': {
		'country': 'austria',
		'population': '1,900,000',
		'fact': 'capital of Austria',
	},
	'Rome': {
		'country': 'italy',
		'population': '2,900,000',
		'fact': 'capital of Italy',
	},
}

for city, info in cities.items():
	print(f"Things I know about {city.title().strip()}."
		f"\nIt's located in {info['country'].title().strip()}."
		f"\nIt has a population of {info['population'].title().strip()} people.")
	if city == 'Klagenfurt':
		print(f"One fact about {city.title().strip()} " 
			f"is that it is {info['fact'].strip()}.\n")
	else:
		print(f"One fact about {city.title().strip()} "
			f"is that it is the {info['fact'].strip()}.\n")