pets = [{'species': 'cat',
	'owners_name': 'marie',
	'pet_name': 'snowball',
	},
	{'species': 'dwarf pig',
	'owners_name': 'karner',
	'pet_name': 'bubi',
	},
	{'species': 'bird',
	'owners_name': 'michael',
	'pet_name': 'tweety',
	},
	{'species': 'hamster',
	'owners_name': 'mark-philipp',
	'pet_name': 'purzel',
	}]

for pet in pets:
	print(f"The pet's species is {pet['species'].strip()}.\n"
		f"The owner's name is {pet['owners_name'].title().strip()}.\n"
		f"The pet's name is {pet['pet_name'].title().strip()}.\n")
