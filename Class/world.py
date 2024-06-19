
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def info_self(self):
        return f"It's class Animal .Name is {self.nickname} and his age is {self.age}"


class Cat(Animal):
    name = ['cat']

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











