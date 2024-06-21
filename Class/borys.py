# Композиція
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"It's class Animal. Name is {self.nickname} and his age is {self.age}"


class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name} - {self.phone}"


class Cat(Animal):
    def __init__(self, nickname, age, name, phone):
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)     # Композиція

    def get_info(self):
        return f"It's class Animal. Name is {self.nickname} and his age is {self.age}"

    def sound(self):
        return f" {self.nickname} >>> каже : МЯУ-МЯУ"


cat = Cat('Alisa', 7, 'Vlad', '0963610573')
print(cat.owner.info())









