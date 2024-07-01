def describe_city(city, country='austria'):
	print(f"{city.title()} is in {country.title()}")

describe_city('Klagenfurt')
describe_city('Wien')
describe_city(country='Germany', city='München')