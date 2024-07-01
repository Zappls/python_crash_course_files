from restaurant import Restaurant

class Flavors:
    def __init__(self):
        self.flavors = []

    def add_flavors(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(self.flavors)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = Flavors()

my_stand = IceCreamStand('NicesIce', 'Ice Cream')
my_stand.flavors.add_flavors('Vanilla')
my_stand.flavors.add_flavors('Choco')
my_stand.flavors.display_flavors()
