cities = {
	'Klagenfurt': {
		'country': 'Austria',
		'population': '100,000',
		'fact': 'my birthplace',
	},
	'Vienna': {
		'country': 'Austria',
		'population': '1,900,000',
		'fact': 'capital of Austria',
	},
	'Rome': {
		'country': 'Italy',
		'population': '2,900,000',
		'fact': 'capital of Italy',
	},
	'Paris': {
		'country': 'France',
		'population': '2,200,000',
		'fact': ['The captial of France', 'A shithole'],
	},
}

for city, info in cities.items():
	print(f"Things I know about {city.title().strip()}."
		f"\nIt's located in {info['country'].title().strip()}."
		f"\nIt has a population of {info['population'].title().strip()} people.")
	if city == 'Klagenfurt':
		print(f"One fact about {city.title().strip()} " 
			f"is that it is {info['fact']}.\n")
	elif city == 'Paris':
		print(f"Facts about {city.title().strip()} " 
			f"are that it is: ")
		for v in info['fact']:
			print(f"{v}.")
	else:
		print(f"One fact about {city.title().strip()} "
			f"is that it is the {info['fact']}.\n")