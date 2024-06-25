# Контейнер UserString
from collections import UserString


templase = [
    " Ви можете досягти всього. ",
    " Прості щоденні справи допоможуть досягти успіху ",
    " Боротись з прокрастинацією не складно "
]

#for item, text in enumerate(templase):
    #print("|{:^5}|{:<15}".format(item, text))
class Text(UserString):
    def set_limit_text(self, limit=30):
        return (f"{self.data[: limit -3]} ...")


text = [Text(text) for text in templase]
for item, text in enumerate(text):
    print("|{:^5}|{:<15}".format(item, text.set_limit_text()))







