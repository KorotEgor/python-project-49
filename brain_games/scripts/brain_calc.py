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
    return solution_of_expression, expression

def calculate():
    question = 'What is the result of the expression?'
    base_for_games.greetings(question)
    counter_correct_answers = 0
    while counter_correct_answers < 3:
        solution_of_expression, expression = find_solution()
        solution_of_expression = str(solution_of_expression)
        if base_for_games.checking_for_correctness(expression, solution_of_expression):
            counter_correct_answers += 1
    base_for_games.congratulations()


if __name__ == '__main__':
    calculate()
