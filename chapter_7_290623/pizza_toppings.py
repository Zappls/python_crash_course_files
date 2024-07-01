prompt = "Please enter your desired toppings:"
prompt += "\nType 'quit' when you are finished."

flag = True
while flag:
	topping = input(prompt)
	if topping == 'quit':
		flag = False
	else:
		print(f"Added {topping.strip()} to your pizza!")