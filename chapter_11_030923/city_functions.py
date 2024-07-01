def city_country_string(city, country, population=''):
	if population:
		full_name = f"{city.title()}, {country.title()} - population {population}"
	else:
		full_name = f"{city.title()}, {country.title()}"
	return full_name