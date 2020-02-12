class Car(): 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading= 0
        self.rims= 4
        self.door= 4
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make + " "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")
    def update_odometer(self, mileage):
        """Modifica el valor del metodo desde la funcion"""
        self.odometer_reading = mileage
    def num_rims(self):
        print("This car has " + str(self.rims) + " rims")
    def update_rims(self, wheels):
        """Modifica el valor del metodo desde la funcion"""
        self.rims = wheels
    def num_doors(self):
        print("This car has " + str(self.doors) + " doors.")
    def update_doors(self,car_doors ):
        """Modifica el valor del metodo desde la funcion"""
        self.doors =car_doors 
        
        

my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(120)
my_new_car.read_odometer()
my_new_car.update_rims(6)
my_new_car.num_rims()
my_new_car.update_doors(8)
my_new_car.num_doors()