#!/usr/bin/env python

from brain_games.cli import rounds
from brain_games.games.prime import prime


def main():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rounds(prime, task)


if __name__ == '__main__':
    main()
