import random


def even():
    number = random.randint(0, 1000)
    if number % 2:
        return ('no', number)
    else:
        return ('yes', number)
