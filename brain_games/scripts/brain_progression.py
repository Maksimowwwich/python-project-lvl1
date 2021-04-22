#!/usr/bin/env python

from brain_games.cli import rounds
from brain_games.games.progression import progression


def main():
    task = 'What number is missing in the progression?'
    rounds(progression, task)


if __name__ == '__main__':
    main()
