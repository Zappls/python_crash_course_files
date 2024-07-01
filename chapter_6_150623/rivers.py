rivers = {'nile': 'egypt', 'donau': 'austria', 'drau': 'austria'}

for key, value in rivers.items():
	print(f'The {key.title()} runs through {value.title()}.')

for key in rivers.keys():
	print(key)

for value in rivers.values():
	print(value)