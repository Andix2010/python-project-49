import random

from brain_games.general_engine import run_game

OPERATIONS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }


def run_calc_game(name: str) -> None:
    run_game(get_calc_round, name, "What is the result of the expression?")


def get_calc_round() -> tuple:
    number_one = random.randint(1, 40)
    number_two = random.randint(1, 40)
    operator = random.choice(['+', '-', '*'])
    right_answer = str(OPERATIONS[operator](number_one, number_two))
    return (f"{number_one} {operator} {number_two}", right_answer)