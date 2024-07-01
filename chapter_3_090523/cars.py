cars = ['bmw', "audi", "toyota", "subaru"]
cars.sort()
print(cars)
# permanently sorted. Original order not saved.
cars = ['bmw', "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)
# also permanently sorted but in reverse order.
cars = ['bmw', "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)
# sort sorts permanently, sorted sorts temporarily.
cars.reverse()
print("\nHere is the original list reversed:")
print(cars)
# reverse() changes the order of the list permanently.
cars.reverse()
print(len(cars))



