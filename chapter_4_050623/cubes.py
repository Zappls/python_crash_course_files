cubes = list(range(1,11))
for value in cubes:
	value = value**3
	print(value)

cubes = [value**3 for value in range(1,11)]
for value in cubes:
	print(value)