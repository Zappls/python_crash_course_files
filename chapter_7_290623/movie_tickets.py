prompt = "Please enter your age: "


flag = True
while flag:
	age = input(prompt)
	if age == 'quit':
		flag = False
		break
	else:
		age = int(age)
	if age < 3:
				print(f"Your ticket is free since you are {age} years old!")
				
	elif age <= 12:
				print(f"Your ticket costs $10 since you are {age} years old!")
				
	elif age > 12:
				print(f"Your ticket costs $15 since you are {age} years old!")
				
	else:
		break
		
