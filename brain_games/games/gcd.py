import random


def get_gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return str(x)


def gcd():
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 200)
    return (get_gcd(number1, number2), f'{number1} {number2}')
