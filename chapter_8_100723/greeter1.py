def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me you name:")
	print("(enter 'quit' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'quit':
		break
	l_name = input("Last name: ")
	if l_name == 'quit':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")
	