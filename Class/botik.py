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
    pass


class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number format.")


class Email(Field):
    def __init__(self, value):
        self.value = value
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, value):
            super().__init__(value)
        else:
            raise ValueError("Invalid email")


class Birthday(Field):
    def __init__(self, value):
        self.value = value
        date_format = "%Y-%m-%d"
        parsed_date = datetime.strptime(value, date_format).date()
        if parsed_date > datetime.now().date():
            raise ValueError(
                Fore.LIGHTRED_EX + "Birthday date cannot be in the future"
            )
        super().__init__(value)



class Record:

    def __init__(self, name, phone, email, birthday ):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"{Fore.MAGENTA}Name: {self.name}\n{Fore.RED}Phone: {self.phone}\n{Fore.CYAN}Email: {self.email}\n{Fore.YELLOW}Birthday: {self.birthday}{Fore.RESET}"

class AddressBook(UserList):
    def add_record(self, record):
        self.append(record)

    def find_record(self, name):
        for record in self:
            if record.name == name:
                return record
        return None

    def remove_record(self, name):
        record = self.find_record(name)
        if record:
            self.remove(record)
        else:
            print(Fore.LIGHTRED_EX + "Record not found.")

    def update_record(self, name, phone=None, email=None, birthday=None):
        record = self.find_record(name)
        if record:
            if phone:
                record.phone = Phone(phone)
            if email:
                record.email = Email(email)
            if birthday:
                record.birthday = Birthday(birthday)
        else:
            print(Fore.LIGHTRED_EX + "Record not found.")


if __name__ == '__main__':
    phone = Phone('0963610573')
    print(Fore.RED + phone.value)
    name = Name('Luda')
    print(Fore.MAGENTA + name.value)
    email = Email('luda80@gmail.com')
    print(Fore.CYAN + email.value)
    birthday = Birthday('1980-05-16')
    print(birthday.value)
    contact = Record('Vlad любимий син', '0631934048', 'vlad2000@gmail.com', '2000-01-28')
    print(contact)
    contact1 = Record('Luda','0963610573', 'luda80@gmail.com', '1980-05-16')
    print(contact1)
    contact1.name = 'Alissa'
    print(contact1)
    address_book = AddressBook()
    address_book.add_record(contact)
    address_book.add_record(contact1)
    print('All contacts :')
    for contact in address_book:
        print(contact)

        print("\nFind contact Vlad:")
        print(address_book.find_record('Vlad'))

        print("\nUpdate contact Vlad:")
        address_book.update_record('Vlad', phone='0630000000')
        print(address_book.find_record('Vlad'))

        print("\nRemove contact Luda:")
        address_book.remove_record('Luda')
        print("All contacts:")
        for record in address_book:
            print(record)