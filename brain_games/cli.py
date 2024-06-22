import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    return name


def greetings(question):
    print(question)


def question(expression):
    print(f'Question: {expression}')

    return prompt.string('Your answer: ')


def checking_for_correctness(name, answer, solution):
    if solution == answer:
        print('Correct!')

        return True

    print(f"'{answer}' is wrong answer ;(. Correct answer was '{solution}'.")
    print(f"Let's try again, {name}!")

    return False


def congratulations(name):
    print(f'Congratulations, {name}!')
