usernames = ['admin', 'alex', 'andi', 'steve', 'chad']

for user in usernames:
	if user == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
		print(f'Hello {user.title().strip()}, thank you for logging in again.')