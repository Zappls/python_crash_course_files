favorite_numbers = {'alex': '27',
	'andi': '69',
	'chad': '6',
	'peter': '7',
	'marie': '10',
}
number = favorite_numbers.get('alex')
print(f"Alex' favorite number is {number}.")
number = favorite_numbers.get('andi')
print(f"Andi's favorite number is {number}.")
number = favorite_numbers.get('chad')
print(f"Chad's favorite number is {number}.")
number = favorite_numbers.get('peter')
print(f"Peter's favorite number is {number}.")
number = favorite_numbers.get('marie')
print(f"Marie's favorite number is {number}.")

for key, value in favorite_numbers.items():
	print(f"Key: {key}")
	print(f"Value: {value}")