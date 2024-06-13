import re
from typing import Callable

t = ("Загальний дохід працівника складається з декількох частин:\n"
     "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")


def generator_numbers(text: str):
    numbers = re.findall(r'\b-?\d+\.\d+\b', text)
    for el in numbers:
        yield float(el)


def sum_profit(text: str, func: Callable):
    numbers = func(text)
    total = sum(numbers)
    return total


res = generator_numbers(t)
res_sum = sum_profit(t, generator_numbers)

print(res)
print(res_sum)
