from tabulate import tabulate


headers = ["ім'я", "телефон"]
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


def add_contact(args: tuple, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Контакт оновлено'
    else:
        contacts[name] = phone
        return 'Контакт додано'


def show_all_contacts(contacts: dict) -> str:
    contacts = [[name, phone] for name, phone in contacts.items()]
    table = tabulate(contacts, headers=headers, tablefmt="grid")
    return table


def show_contact(args: tuple, contacts:dict) -> str:
    name = args[0]
    phone = contacts.get(name, "Контакт не знайдено")
    contact = [[name, phone]]
    table = tabulate(contact, headers=headers, tablefmt='grid')
    return table



def main():
    contacts = {}
    print("Ласкаво просимо в асистент бота!!!>>>")

    while True:
        user_input = input("Введіть вашу команду : >>> ").strip().lower()
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print("До побачення!!!")
            break
        elif command == "привіт":
            print("Привіт чим можу допомогти?")
        elif command in ["add", "change"]:
            print(add_contact(args, contacts))
        elif command == 'all':
            print(show_all_contacts(contacts))
        elif command == 'show_phone':
            print(show_contact(args, contacts))

        else:
            print("Ви ввели некоректну команду!!!")


if __name__ == "__main__":
    main()
