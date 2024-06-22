# Контейнер UserList
from collections import UserList
from random import randint


class MyList(UserList):
    info = 'This is my list class'

    def get_positive(self):
        return list(filter(lambda x: x > 0, self.data))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))

    def get_info(self):
        return self.info


r = []
for _ in range(0, 35):
    r.append(randint(-10, 10))

r.append(90)

result = MyList(r)
print(result)
print(result.get_positive())
print(result.get_negative())
print(result.get_info())







