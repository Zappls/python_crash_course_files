cubes = list(range(1,11))
for value in cubes:
	value = value**3
	print(value)

cubes = [value**3 for value in range(1,11)]
for value in cubes:
	print(value)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[4:7])

print("The last three items in the list:")
print(cubes[-3:])