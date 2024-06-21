

class Dog():

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name != self._name:
            print("ІНКАПСУЛЯЦІЯ")


    def do_volume(self):
        print(f"{self.name} says gay gay \n{self.age} лет собачке")

    def __str__(self):
        return f"name:{self.name}\nage:{self.age}\n"
alisa = Dog("Alica", 6)  # Create exzem class
#print(alisa.name)
alisa.name = "Pusha"
alisa.age = 12
print(alisa)
