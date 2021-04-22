#!/usr/bin/env python

from brain_games.cli import rounds
from brain_games.games.gcd import gcd


def main():
    task = 'Find the greatest common divisor of given numbers.'
    rounds(gcd, task)


if __name__ == '__main__':
    main()
