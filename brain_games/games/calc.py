import random


def calc():
    number1 = random.randint(0, 50)
    number2 = random.randint(0, 50)
    signs = ['-', '+', '*']
    sign = random.choice(signs)
    if sign == '-':
        right_answer = str(number1 - number2)
    elif sign == '+':
        right_answer = str(number1 + number2)
    elif sign == '*':
        right_answer = str(number1 * number2)
    return (right_answer, (number1, sign, number2))
