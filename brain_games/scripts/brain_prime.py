#!/usr/bin/env python3

import random

from brain_games.scripts import base_for_games


def find_solution():
    expression = random.randint(1, 100)

    if expression < 2:
        return 'no', expression

    for i in range(2, int(expression ** 0.5 + 1)):
        if not (expression % i):
            return 'no', expression

    return 'yes', expression


def is_prime():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    is_prime()
