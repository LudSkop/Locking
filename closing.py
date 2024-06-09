a = 5


def outer_function(x):
    y = 10

    def inner_function():
        result = x * y
        print(f'Result is :>> {result}')

    return inner_function


author = outer_function(a)
author()
