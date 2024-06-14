
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f'Name : {self.nickname}, age : {self.age}'


value = Animal('Alisa', 6)
print(value)
print(value.nickname)
print(value.age)
print(value.get_info())
value.age = 4
value.nickname = 'Pusha'
print(value.get_info())





