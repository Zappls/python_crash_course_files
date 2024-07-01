filename = 'guest_book.txt'

while True:
	prompt = input("What is your name? ")
	if prompt == "admin_exit":
		break
	print(f"Welcome to our establishment {prompt.title()}!")
	with open(filename, 'a') as file_object:
		file_object.write(f"{prompt}\n")
