# Наслідування
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def info_self(self):
        return f"It's class Animal .Name is {self.nickname} and his age is {self.age}"


class Cat(Animal):
    name = ['Cat']

    def __init__(self, nickname, age, owner):
        super().__init__(nickname, age)
        self.owner = owner

    def saund(self):
        return f'{self.nickname} says meeey '

    def info_self(self):
        return 3 * 10


cat = Cat('Alisa', 6, 'Vladyclav')
print(cat.nickname)
print(cat.age)
print(cat.owner)
print(cat.info_self())
print(cat.saund())

cat_2 = Cat('Borys', 9, 'Ivan')
print(cat_2.name)
cat.name[0] = 'Luda'

print(cat.name)
print(cat_2.nickname)
print(cat_2.age)
print(cat_2.owner)


class Car:
    brand = 'Toyota'


p1 = Car()
p2 = Car()
print(p1.brand)
print(p2.brand)

Car.brand = 'Opel'

print(p1.brand)
print(p2.brand)
print(dir(cat))
print(dir(cat_2))# Показує всі атрибути і поля в екземплярі( в кінці будуть наші)









