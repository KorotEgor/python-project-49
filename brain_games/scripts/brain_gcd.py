#!/usr/bin/env python3

import random
import math

from brain_games.scripts import base_for_games


def find_solution():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    expression = f'{first_number} {second_number}'
    solution_of_expression = math.gcd(first_number, second_number)
    return str(solution_of_expression), expression


def greatest_common_divisor():
    question = 'Find the greatest common divisor of given numbers.'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    greatest_common_divisor()
