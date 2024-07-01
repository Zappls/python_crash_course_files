pizzas = ["Käsepizza", "Pizza Hawaii Deluxe", "Pizza Carpicosa"]
friend_pizzas = pizzas[:]
pizzas.append("Salami")
friend_pizzas.append("Diavolo")
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
