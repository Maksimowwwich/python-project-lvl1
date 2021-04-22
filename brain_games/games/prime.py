import random


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime():
    number = random.randint(1, 200)
    if is_prime(number):
        return ('yes', number)
    else:
        return ('no', number)
