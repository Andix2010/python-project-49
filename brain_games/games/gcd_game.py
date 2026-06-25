import random

from brain_games.general_engine import run_game


def run_gcd_game(name: str) -> None:
    run_game(get_gcd_round, name, 
            'Find the greatest common divisor of given numbers.')
        

def get_gcd_round() -> tuple:
    number_one = random.randint(1, 40)
    number_two = random.randint(1, 40)
    a = number_one
    b = number_two

    while b != 0:
        a, b = b, a % b
    right_answer = str(a)

    return (f"{number_one} {number_two}", right_answer)