filename_cats = 'cats.txt'
filename_dogs = 'dogs.txt'

with open(filename_cats, 'w') as fc:
	fc.write('\nSnowball\nCookie\nYuuki')

with open(filename_dogs, 'w') as fd:
	fd.write('\nKevin\nBuddy\nRex')

try:
	with open(filename_cats, 'r') as fc:
		cats = fc.read()
	with open(filename_dogs, 'r') as fd:
		dogs = fd.read()
except FileNotFoundError:
	print("The file you are trying to open was not found.")
else:
	print(f"The cats names are: {cats}\n"
	f"\nThe dogs names are: {dogs}")


 