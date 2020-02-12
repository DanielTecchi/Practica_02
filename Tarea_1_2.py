class restaurant():
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_res(self):
        print("El restaurante " + self.restaurant_name.title() + " trabaja comida " + self.cuisine_type.title())
    def open_restaurant(self):
        print( self.restaurant_name.title()  +" abre de lunes a sabado de 9:30am a 23:00hrs")
    def customers(self):
        print("Contamos con "+ str(self.number_served)+" clientes en estancia.")
    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers
        else: print ("You cannot do that")

my_restaurant=restaurant("the cruw", "americana")
my_restaurant.describe_res()
my_restaurant.open_restaurant()
my_restaurant.number_served=32
my_restaurant.customers()