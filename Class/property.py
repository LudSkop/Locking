class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None

        self.nickname = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Тварина має мати ім'я ")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError("Тварина не може мати такий вік ")


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тварина не може мати таку вагу")


a = Animal('Alissa', 5, -1)
print(a.name, a.age, a.weight)

