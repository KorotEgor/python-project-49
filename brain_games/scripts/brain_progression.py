#!/usr/bin/env python3

import random

from brain_games.scripts import base_for_games


def find_solution():
    step_of_progression = random.randint(1, 100)
    amount = random.randint(5, 15)
    start = random.randint(0, 100)
    end = start + step_of_progression * (amount - 1)
    expression = [str(i) for i in range(start, end + 1, step_of_progression)]
    number_of_unknown_number = random.randint(0, amount - 1)
    solution_of_expression = expression[number_of_unknown_number]
    expression[number_of_unknown_number] = '..'
    expression = ' '.join(expression)
    return solution_of_expression, expression


def unknown_progression_number():
    question = 'What number is missing in the progression?'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    unknown_progression_number()
