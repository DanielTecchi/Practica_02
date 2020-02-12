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
    def num_rims(self):
        print("This car has " + str(self.rims) + " rims")
    def num_doors(self):
        print("This car has " + str(self.doors) + " doors.")
        

my_new_car = Car("audi","a4",2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
my_new_car.rims = 6
my_new_car.num_rims()
my_new_car.doors = 8
my_new_car.num_doors()