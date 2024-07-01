class Employee:
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, increase=5000):
		self.increase = increase
		new_salary = int(self.salary) + int(self.increase)
		self.salary = new_salary
		return self.salary


