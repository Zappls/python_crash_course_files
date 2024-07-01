
places = {}
flag = True

while flag:

	name = input('\n\tWhat is your name? ')
	prompt = input('\tIf you could visit one place in the world, where would you go? ')
	places[name] = prompt
	response = input('\tDo you want to continue? Type yes/no ')
	if response == 'yes':
		continue
	if response == 'no':
		flag = False
	
for name, prompt in places.items():
	print(f'\t{name.title().strip()} wants to go to {prompt}.')