

def greeting(name):
    print(f'Hello my name is: {name}')

# Декоратор
def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print('test')
        result = func(*args, **kwargs)
        print('Bye, bye !!!')
    return wrapper


greeting('Alex')
new_greeting = greeting_decorator(greeting)
new_greeting('Olga')



