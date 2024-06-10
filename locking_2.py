# Карінг
def greeting_simple(name, msg):
    return f' {name} {msg}'


print(greeting_simple('Anton', 'Hello world'))
print(greeting_simple('Natalia', 'Go to home'))


def greeting(name):
    def simple(msg):
        return f'{name} {msg}'
    return simple


msg_anton = greeting('Anton')
print(msg_anton('Hello world'))
msg_anton = greeting('Natalia')
print(msg_anton('Go to home'))