# Агрегація
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
    def __init__(self, nickname, age, owner: Owner): # Агрегація(передаємо екземпляр господаря як параметр)
        super().__init__(nickname, age)
        self.owner = owner     # Агрегація

    def get_info(self):
        return f"It's class Animal. Name is {self.nickname} and his age is {self.age}"


owner = Owner('Vlad', '0963610573')
cat = Cat('Pusha', 5, owner)
print(cat.owner.info())









