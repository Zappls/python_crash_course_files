filename_cats = 'cats.txt'
filename_dogs = 'dogs.txt'

try:
	with open(filename_cats, 'r') as fc:
		cats = fc.read()
	with open(filename_dogs, 'r') as fd:
		dogs = fd.read()
except FileNotFoundError:
	pass
else:
	print(f"The cats names are: {cats}\n"
	f"\nThe dogs names are: {dogs}")


 