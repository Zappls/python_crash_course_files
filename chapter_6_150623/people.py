people = {
	'awolfger': {
		'first_name': 'Alexander',
		'last_name': 'Wolfger',
		'age': '29',
		'city': 'Klagenfurt',
	},
	'mwolfger': {
		'first_name': 'Maria',
		'last_name': 'Wolfger',
		'age': '60',
		'city': 'Klagenfurt',
	},
	'ttorta': {
		'first_name': 'Thomas',
		'last_name': 'Torta',
		'age': '29',
		'city': 'Graz',
	},
}
for username, user_info in people.items():
	print(f"Username: {username}")
	fullname = (f"{user_info['first_name']} {user_info['last_name']}")
	print(f"Full name: {fullname}")
	print(f"Age: {user_info['age']}")
	print(f"city: {user_info['city']}\n")