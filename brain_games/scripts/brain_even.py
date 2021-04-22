#!/usr/bin/env python

from brain_games.cli import rounds
from brain_games.games.even import even


def main():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    rounds(even, task)


if __name__ == '__main__':
    main()
