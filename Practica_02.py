print ("CLASES")
print ("\n")

"""Ejercicio 1: Capture el c´odigo y observe lo que aparece en la terminal, 
   guarde el co´digo como Ejercicio_01.py y suba el c´odigo a un nuevo repositrio
   en GitHub llamado Practica_02"""
class Car(): 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
        
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make + " "+self.model
        return long_name.title()
my_new_car = Car("audi","a4",2020) 
print(my_new_car.get_descriptive_name())



