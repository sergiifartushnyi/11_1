def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_generator(end):
    """Генерує прості числа до верхньої межі end."""
    num = 2
    while num <= end:
        if is_prime(num):
            yield num
        num += 1

from inspect import isgenerator

gen = prime_generator(1)

print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
print('Ok')