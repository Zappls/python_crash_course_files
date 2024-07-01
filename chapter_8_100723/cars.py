def make_car(manufacturer, model_name, **kwargs):
	kwargs['manufacturer'] = manufacturer
	kwargs['model_name'] = model_name
	return kwargs

my_car = make_car('Audi', 'S8', heated_seats='Yes', color='Black', horsepower='All of it',)
print(my_car)