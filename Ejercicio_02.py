class Car(): 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading= 0
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make + " "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n")
class Car(): 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make + " "+self.model
        return long_name.title()
    def read_odometer(self):
        self.odometer_reading= 0
        print("This car has " + str(self.odometer_reading) + " miles on it")

my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""Se detecto que en la escritura del codigo uno de los parametros tenia un error
    de orden de escritura ya que habia puesto sefl en vez de self esa fue la pro-
    blematica del programa"""
print("\n")
my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n")
class Car(): 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
        self.rims= 4
        self.door= 4
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make + " "+self.model
        return long_name.title()
    def read_odometer(self):
        self.odometer_reading= 0
        print("This car has " + str(self.odometer_reading) + " miles on it")
    def num_rims(self):
        print("This car has " + str(self.rims) + " rims")
    def num_doors(self):
        print("This car has " + str(self.door) + " doors.")
        

my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.num_rims()
my_new_car.num_doors()