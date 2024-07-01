from random import randint
class Die:
	def __init__(self, sides=6, rolls=1):
		self.sides = sides
		self.rolls = rolls

	def roll_die(self):
		while self.rolls >=1:
			print(f'Your {self.sides}-sided die rolled: {randint(1, self.sides)}.')
			self.rolls -= 1

d6 = Die()
d6.roll_die()

d10 = Die(sides=10, rolls=5)
d10.roll_die()

d20 = Die(sides=20, rolls=2)
d20.roll_die()