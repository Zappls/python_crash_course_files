dimensions = (200, 50) #tuples are lists that can't be changed.
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)

#Can't modify a tuple but you can assign a new value
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)