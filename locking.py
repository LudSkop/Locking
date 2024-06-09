
def outer(a: str):
    b = 'Oleg'

    def inner():
        result = a + ' ' + b
        print(result)
    return inner


name = outer('liuda')
name()












