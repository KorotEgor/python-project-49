#!/usr/bin/env python3

import prompt

from brain_games.scripts import brain_games


name = brain_games.main()

def greetings(question):
    print(question)

def checking_for_correctness(expression, solution_of_expression):
    print(f'Question: {expression}')
    user_answer = prompt.string('Your answer: ')
    if solution_of_expression == user_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{solution_of_expression}'.")
        print(f"Let's try again, {name}!")
        return False

def congratulations():
    print(f'Congratulations, {name}!')
