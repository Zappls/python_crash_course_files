def addition():
	"""Adds the 2 arguments, 
	prints an error message if the input is not a number."""
	number1 = input("Type in the first number you wish to add: ")
	number2 = input("Type in the second number you wish to add: ")
	try:
		result = int(number1) + int(number2)
	except ValueError:
		print("Only numbers can be added!")
	else:
		print(f"The result is {result}.")


addition()
