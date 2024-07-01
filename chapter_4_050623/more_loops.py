my_foods = ["pizza", "falafel", "carrot cake"]
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

my_foods.append("cannoli")
friends_food.append("ice cream")

print("\nMy favorite foods are:")
for value in my_foods:
	print(value)
print("\nMy friend's favorite foods are:")
for value in friends_food:
	print(value)
