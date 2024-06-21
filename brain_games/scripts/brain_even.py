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
    base_for_games.greetings(question)
    counter_correct_answers = 0
    while counter_correct_answers < 3:
        solution_of_expression, expression = find_solution()
        if base_for_games.checking_for_correctness(expression, solution_of_expression):
            counter_correct_answers += 1
    base_for_games.congratulations()


if __name__ == '__main__':
    main()
