# ПОЛІМОРФІЗМ
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"It's class Animal. Name is {self.nickname} and his age is {self.age}"


class Cat(Animal):
    def __init__(self, nickname, age, owner):
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f'{self.nickname} says Мяу '

    def get_info(self):
        return 3 * 10


class Dog(Animal):

    def __init__(self, nickname, age, owner):
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f' {self.nickname} says Гав'

    def get_info(self):
        return f"It's class Animal. Name is {self.nickname} and his age is {self.age}"


cat = Cat('Alisa', 7, 'Vlad')
dog = Dog('Pusha', 5, 'Oleg')

print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(isinstance(dog, Dog))
print('=================')
print(type(dog) is Animal)
print(type(dog) is Dog)
for element in (cat, dog):
    print(element.sound())

