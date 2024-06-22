from brain_games import cli


def run_game(question, game_fn, wins=3):
    name = cli.welcome_user()
    cli.greetings(question)

    counter_correct_answers = 0
    while counter_correct_answers < wins:
        solution_of_expression, expression = game_fn()
        user_answer = cli.question(expression)
        if cli.checking_for_correctness(
            name,
            user_answer,
            solution_of_expression,
        ):
            counter_correct_answers += 1
        else:
            return

    cli.congratulations(name)
