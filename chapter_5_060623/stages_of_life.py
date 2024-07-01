variable_age = 58

if variable_age < 2:
	person = 'baby'
elif variable_age < 4:
	person = 'toddler'
elif variable_age < 13:
	person = 'kid'
elif variable_age < 20:
	person = 'teenager'
elif variable_age < 65:
	person = 'adult'
else:
	person = 'elder'
print(f'The person is a {person}.')