import random

from brain_games.general_engine import run_game


def run_even_game(name: str) -> None:
    run_game(get_even_round, name, 
            'Answer "yes" if the number is even, otherwise answer "no".')
        

def get_even_round():
    number = random.randint(1, 99)
    right_answer = 'yes' if (number % 2 == 0) else 'no'
    return (str(number), right_answer)