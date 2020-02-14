class user():
    def __init__(self, frist_name, last_name, date_nac, age, pasword):
        self.frist_name=frist_name
        self.last_name=last_name
        self.date_nac=date_nac
        self.age=age
        self.pasword=pasword
        self.attempt_user = 0
        self.reset = 0
    def describe_user(self):
        print("Usuaerio: "+self.frist_name+"Fecha de nacimiento: "+self.date_nac+"Edad: "+self.age+"Su contraseña es: "+self.pasword)
    def greet_user(self):
        print("Hola " + self.frist_name + self.last_name + " bienvenido al ipn.")
    def increment_login_attempts(self, user):
            if user <= 10:
                self.attempt_user = user
            else:
                print ('you tried too many times to log in')
    
    def reset_attempts(self):
            self.reset=self.attempt_user
    
    def secure_account(self):
            print('Has alcansado el limete de inicio de secion ' + str(self.attempt_user) + ' ya no se pueden mas')

my_user=user("Jose Daniel ", "Tecchi Perez", "13/dic/2000", "19", "2020302278")
my_user.describe_user()
my_user.greet_user()
my_user.attempt_user=5
my_user.secure_account()
