#!/usr/bin/env python3

import random

from brain_games.scripts import base_for_games


def find_solution():
    step_of_progression = random.randint(0, 100)
    number_of_progression_numbers = random.randint(5, 15)
    start_of_progression = random.randint(0, 100)
    end_of_progression = start_of_progression + step_of_progression * (number_of_progression_numbers - 1)
    expressoin = [str(i) for i in range(start_of_progression, end_of_progression + 1, step_of_progression)]
    number_of_unknown_number = random.randint(0, number_of_progression_numbers - 1)
    solution_of_expression = expressoin[number_of_unknown_number]
    expressoin[number_of_unknown_number] = '..'
    expressoin = ' '.join(expressoin)
    return solution_of_expression, expressoin


def unknown_progression_number():
    question = 'What number is missing in the progression?'
    base_for_games.run_game(question, find_solution)


if __name__ == '__main__':
    unknown_progression_number()
