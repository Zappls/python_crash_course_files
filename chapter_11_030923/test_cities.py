import unittest
from city_functions import city_country_string

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Does an input like 'Santiago, Chile' work?"""
		city_name = city_country_string('santiago', 'chile')
		self.assertEqual(city_name, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Does an input like 'Santiago, Chile - population 5000000' work?"""
		city_name = city_country_string('santiago', 'chile', 'population=5000000')
		
if __name__ == '__main__':
	unittest.main()

