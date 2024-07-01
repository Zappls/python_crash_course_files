from random import choice
lottery = [5, 1, 12, 45, 23, 67, 34, 65, 43, 9, 'A', 'B', 'C', 'D', 'E']

first_digit = choice(lottery)
second_digit = choice(lottery)
third_digit = choice(lottery)
forth_digit = choice(lottery)
winning_ticket = [first_digit, second_digit, third_digit, forth_digit]
print(f'The winning ticket is: {winning_ticket}')


my_ticket = [1, 5, 9, 12]
counter = 0
while my_ticket != winning_ticket:
	first_digit = choice(lottery)
	second_digit = choice(lottery)
	third_digit = choice(lottery)
	forth_digit = choice(lottery)
	winning_ticket = [first_digit, second_digit, third_digit, forth_digit]
	counter += 1
print(f'My ticket {my_ticket} equaled {winning_ticket} after {counter} attempts.')

