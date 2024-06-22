#!/usr/bin/env python3

import random

from brain_games.scripts import base_for_games


def find_solution():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    sign = random.choice(['+', '-', '+'])
    expression = f'{first_number} {sign} {second_number}'
    solution_of_expression = 0
    match sign:
        case '+':
            solution_of_expression = first_number + second_number
        case '-':
            solution_of_expression = first_number - second_number
        case '*':
            solution_of_expression = first_number * second_number
    return str(solution_of_expression), expression

def calculate():
    question = 'What is the result of the expression?'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    calculate()
