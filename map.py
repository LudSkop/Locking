from functools import reduce


def add(x) -> bool:
    if x > 0:
        return True





numb = [num for num in range(2, 5)]
print(numb)

result = list(map(lambda num: num ** 2, numb))

result = list(result)
res = (filter(add, list(result)))
print(res)
print(list(res))
print(type(result))






