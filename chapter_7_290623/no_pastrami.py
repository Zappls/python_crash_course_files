sandwich_orders = ['Tomato-Mozzarella sandwich', 
'BLT-sandwich', 'Pulled Pork-sandwich', 'Pastrami-sandwich', 'Pastrami-sandwich'
,'Pastrami-sandwich']
finished_sandwiches = []
print('We ran out of pastrami! Please order something else.\n')

while 'Pastrami-sandwich' in sandwich_orders:
	sandwich_orders.remove('Pastrami-sandwich')

while sandwich_orders:
	popped_sandwich = sandwich_orders.pop()
	print(f'Making your {popped_sandwich}!')
	finished_sandwiches.append(popped_sandwich)

print(f'\nThe sandwiches we made today are:')
for sandwich in finished_sandwiches:
	print(sandwich)
