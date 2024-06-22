#!/usr/bin/env python3

import sympy

import random

from brain_games.scripts import base_for_games


def find_solution():
    expression = random.randint(1, 100)
    if sympy.isprime(expression):
        return 'yes', expression
    return 'no', expression


def is_prime():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    is_prime()
