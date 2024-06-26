from tabulate import tabulate


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return 'Give me name and phone please'
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner


headers = ["ім'я", "телефон"]


@input_error
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


@input_error
def add_contact(args: tuple, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Контакт оновлено'
    else:
        contacts[name] = phone
        return 'Контакт додано'


@input_error
def show_all_contacts(contacts: dict) -> str:
    contacts = [[name, phone] for name, phone in contacts.items()]
    table = tabulate(contacts, headers=headers, tablefmt="grid")
    return table


@input_error
def show_contact(args: tuple, contacts: dict) -> str:
    name = args[0]
    phone = contacts.get(name, "Контакт не знайдено")
    contact = [[name, phone]]
    table = tabulate(contact, headers=headers, tablefmt='grid')
    return table


@input_error
def main():
    contacts = {}
    print("Ласкаво просимо в асистент бота!!!>>>")

    while True:
        user_input = input("Введіть вашу команду : >>> ").strip().lower()
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print("До побачення!!!")
            break
        elif command == 'hello':
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
