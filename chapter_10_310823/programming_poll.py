filename = "programming_poll.txt"

while True:
	print(f"Why do you like programming?"
		f"\nEnter a reason or type 'quit' to end the programm:\n")
	prompt = input()
	if prompt == 'quit':
		break
	with open(filename, 'a') as file_object:
		file_object.write(f"{prompt}\n")