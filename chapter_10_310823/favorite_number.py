import json

filename = 'favorite_number.json'

favnum = input("What is you favorite number? ")
with open(filename, 'w') as f:
	json.dump(favnum, f)