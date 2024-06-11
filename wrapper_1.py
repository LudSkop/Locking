# Приклад декоратора без args and kwargs

def decorator_name(func):
    def wrapper(firs_name, last_name):
        print('Hello world' * 2)
        res = func(firs_name, last_name)
        return res
    return wrapper


@decorator_name
def full_name(firs_name, last_name):
    print(f'Happe : {firs_name}, {last_name}')


if __name__ == "__main__":
    full_name("Vlad", "Skopenko")