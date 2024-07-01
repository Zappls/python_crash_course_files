current_users = ['armin', 'alex', 'andi', 'steve', 'chad']
for current_user in current_users:
	current_user.lower().strip()

new_users = ['Billy', 'Marie', 'Tony', 'Claire', 'Alex', 'Chad']
for new_user in new_users:
	if new_user.lower().strip() in current_users:
		print(f'The username {new_user} is already taken.')
	else:
		print(f'The username {new_user} is available.')
