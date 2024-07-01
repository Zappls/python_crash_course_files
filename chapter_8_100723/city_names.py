def city_country(city, country):
	geo = f"{city.title()}, {country.title()}"
	return geo

Klagenfurt = city_country('klagenfurt', 'austria')
München = city_country('münchen', 'germany')
Paris = city_country('paris', 'france')

print(Klagenfurt)
print(München)
print(Paris)