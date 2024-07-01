usernames = ['admin', 'alex', 'andi', 'steve', 'chad']

if usernames:
	for user in usernames:
		if user == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(\
				f'Hello {user.title().strip()},thank you for logging in again.')
else:
	print('We need to find some users!')