# Створення декоратора з параметрами


def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(2)
def greeting(name):
    print(f'Hello, my name is : {name}')








if __name__ == "__main__":
    greeting('Vladyslav')
    greeting('Liudmyla')
    greeting('Family')