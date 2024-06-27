# Магічні методи
class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)          # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)          # 20


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)
print(a)