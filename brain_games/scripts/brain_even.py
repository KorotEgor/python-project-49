#!/usr/bin/env python3

import random

from brain_games.scripts import base_for_games


def find_solution():
    expression = random.randint(0, 100)
    solution_of_expression = ''
    if expression % 2 == 0:
        solution_of_expression = 'yes'
    else:
        solution_of_expression = 'no'

    return solution_of_expression, expression


def main():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    main()
