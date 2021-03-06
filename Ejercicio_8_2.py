class Car():
    """Un intento de representar un auto"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
class ElectricCar(Car):
    """Un intento de representar un auto electrico"""
    def __init__(self,make,model,year):
        """ Inicializa los atributos de la clase padre """
        Car.__init__(self,make,model,year)
        
class HybridCar(Car):
    def __init__(self,make,model,year):
        Car.__init__(self,make,model,year)
        self.workswith="2"
    def describe_workswhit(self):
        print("This car works with "+self.workswith+" types of gasoline.")
    def charge(self): 
        print("The battery has been fully charged")
class FuelCar(Car):
    def __init__(self,make,model,year):
        Car.__init__(self,make,model,year)
        self.works="3"
    def describe_work(self):
        print("This car works with "+self.works+" types of energy")
    def charge(self): 
        print("The battery has been fully charged")
        
my_tesla = ElectricCar('tesla','model s',2020)
print(my_tesla.get_descriptive_name())

my_carhybrit=HybridCar("audi","Tecc34","2020")
print(my_carhybrit.get_descriptive_name())
my_carhybrit.describe_workswhit()
my_carhybrit.charge()

my_carfuel=FuelCar("tsuru","47uhs",2020)
print(my_carfuel.get_descriptive_name())
my_carfuel.describe_work()
my_carfuel.charge()