import json

filename = 'favorite_number.json'

def get_fav_number():
	"""Attempts to load users favorite number."""
	try:
		with open(filename, 'r') as f:
			fav_number = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		return None
	else:
		return fav_number

def save_fav_number():
	"""Stores users favorite number."""
	fav_number = input("What is you favorite number? ")
	with open(filename, 'w') as f:
		json.dump(fav_number, f)
	print(f"Thank you! I will remember your favorite number {fav_number}.")
	return fav_number

def fav_number():
	"""Gets favorite number if it exists, otherwise prompts user for it and
		stores it."""
	fav_number = get_fav_number()
	if fav_number == None:
		fav_number = save_fav_number()
	else:
		print(f"I know your favorite number! It's {fav_number}.")

fav_number()