from collections import UserList
import re
from colorama import Fore
from datetime import datetime


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


class Email(Field):
    def __init__(self, email):
        self.email = email
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            super().__init__(email)
        else:
            raise ValueError("Invalid email")


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday
        date_format = "%Y-%m-%d"
        parsed_date = datetime.strptime(birthday, date_format).date()
        if parsed_date > datetime.now().date():
            raise ValueError(
                Fore.LIGHTRED_EX + "Birthday date cannot be in the future"
            )
        super().__init__(birthday)
        #raise ValueError(Fore.BLUE + "Invalid birthday date, format Year-month-day")


class Record:
    pass


class AddressBook(UserList):
    pass


if __name__ == '__main__':
    phone = Phone('0963610573')
    print(Fore.RED + phone.value)
    name = Name('Luda')
    print(Fore.MAGENTA + name.value)
    email = Email('luda80@gmail.com')
    print(Fore.CYAN + email.value)
    birthday = Birthday('1980-05-16')
    print(birthday.value)
