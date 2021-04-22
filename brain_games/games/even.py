import random


def even():
    number = random.randint(0, 1000)
    print(f'Question: {number}')
    if number % 2:
        return 'no'
    else:
        return 'yes'
