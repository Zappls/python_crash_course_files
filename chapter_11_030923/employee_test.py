import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests Employee default and custom raise."""
	def setUp(self):
		"""
		Create a test employee.
		"""
		self.first = 'Alexander'
		self.last = 'Wolfger'
		self.salary = 50000
		self.test_employee = Employee(self.first, self.last, self.salary)

	def test_default_raise(self):
		self.test_employee.give_raise()
		self.assertEqual(self.test_employee.salary, 55000)

	def test_custom_raise(self):
		increase = 10000
		self.test_employee.give_raise(increase)
		self.assertEqual(self.test_employee.salary, 60000)

if __name__ == '__main__':
	unittest.main()