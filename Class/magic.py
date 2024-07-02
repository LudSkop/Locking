# Дано рядок. Повернути новий рядок в якому перший і останній символи помінені місцями
def string(st):
    if len(st) <= 1:
        return st
    return st[-1] + st[1:-1] + st[0]


if __name__ == "__main__":
    print(string('alissa'))













