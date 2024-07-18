from collections import UserList


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if value.isalpha():
            super().__init__(value)
        else:
            raise ValueError("Invalid name  format.")


class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
           super().__init__(value)
        else:
            raise ValueError("Invalid phone number format.")



class Record():
    pass


class AddressBook(UserList):
    pass




if __name__=='__main__':
    phone = Phone("1234567890")
    print(phone.value)
    name = Name('Luda')
    print(name.value)
