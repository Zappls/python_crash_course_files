import json

filename = 'favorite_number.json'

with open(filename, 'r') as f:
	favnum = json.load(f)
	print(f"I know your favorite number! It's {favnum}.")