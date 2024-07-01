favorite_numbers = {'alex': ['27', '69', '420'],
	'andi': ['69', '7', '18'],
	'chad': ['6', '66', '666'],
	'peter': ['7', '8', '9'],
	'marie': ['100', '200', '300'],
}
number = favorite_numbers.get('alex')
print(f"Alex' favorite numbers are {number}.")
number = favorite_numbers.get('andi')
print(f"Andi's favorite numbers are {number}.")
number = favorite_numbers.get('chad')
print(f"Chad's favorite numbers are {number}.")
number = favorite_numbers.get('peter')
print(f"Peter's favorite numbers are{number}.")
number = favorite_numbers.get('marie')
print(f"Marie's favorite numbers are{number}.")

for key, value in favorite_numbers.items():
	print(f"Key: {key}")
	print(f"Value: {value}")

for name, numbers in favorite_numbers.items():
	print(f"{name.title().strip()}'s favorite numbers are:")
	for number in numbers:
		print(number)