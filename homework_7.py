
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0 or n == 1:
            return n
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci


fib = caching_fibonacci()
print(fib(10))
print(fib(15))






