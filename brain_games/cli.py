import prompt


def welcome_user():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rounds(func, task, n=3):
    name = welcome_user()
    print(task)
    for _ in range(n):
        right_answer = func()
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
