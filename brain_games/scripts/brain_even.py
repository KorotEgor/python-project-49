#!/usr/bin/env python3

import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_correct_answers = 0
    while counter_correct_answers < 3:
        random_number = random.randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0) == (user_answer == 'yes'):
            print('Correct!')
            counter_correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
