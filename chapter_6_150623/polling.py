favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward':'ruby',
	'phil': 'python',
}
people = ['jen', 'alex', 'brad', 'phil', 'joe']

for value in people:
	if value in favorite_languages.keys():
		print(f'Thanks for responding {value.title()}.')
	else:
		print(f'Please take our poll {value.title()}.')
