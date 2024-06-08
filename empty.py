name = ("ludmila", 'oleg')
phone = (234, 4456)
dict = {}
dict[name[0]] = phone[0]
dict[name[1]] = phone[1]

print(dict)

for el, al in zip(name, phone):
     dict[el] = al


# Функція може бути збережена у змінній чи структурі даних
def mul(a, b):
    return a * b


temp_value = mul(3, 5)
print(temp_value)


temp_value = mul
result = temp_value(3, 5)
print(result)
print(temp_value)


fieled = {
    'a': 5,
    'b': 3,
    'operation': temp_value
}

res = fieled.get('operation')(fieled.get('a'), fieled.get('b'))
print(res)
f = fieled.get('operation')
res_1 = f(5, 3)
print(res_1)

#друга вимога - функція може бути передана в іншу функцію
def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def oper(a, b, func):
    return func(a, b)


result_mul = oper(7, 9, mul)
print(result_mul)

result_sub = oper(6, 9, sub)
print(result_sub)

# Третя вимога - функція може бути повернена з функції як результат


def mul(a, b):
    return a * b


def sub(a, b):
    return a + b


def ops(operator: str):
    if operator == '*':
        return mul
    elif operator == '+':
        return sub
    else:
        pass


