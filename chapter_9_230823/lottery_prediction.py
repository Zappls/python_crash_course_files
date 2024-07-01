from random import shuffle, choice

numbers = []
for i in range(1, 46):
    numbers.append(i)

drawing = []
shuffle(numbers)

while len(drawing) < 6:
	drawing.append(numbers.pop())
	shuffle(numbers)

drawing.sort()

print(f'The numbers are:{drawing}.')

