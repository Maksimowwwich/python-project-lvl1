#!/usr/bin/env python


from brain_games.cli import rounds
from brain_games.games.calc import calc


def main():
    task = 'What is the result of the expression?'
    rounds(calc, task)


if __name__ == '__main__':
    main()
