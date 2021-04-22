import random


def progression():
    first = random.randint(0, 100)
    step = random.randint(4, 15)
    numbers = random.randint(5, 10)
    missing_index = random.randint(0, numbers - 1)
    missing_number = str(first + step * missing_index)
    question = [(first + step * i) if (i != missing_index)
                else '..' for i in range(numbers)]
    return (missing_number, question)
