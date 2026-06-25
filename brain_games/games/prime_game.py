import random

from brain_games.general_engine import run_game


def run_prime_game(name: str) -> None:
    run_game(get_prime_round, name, 
            'Answer "yes" if given number is prime. Otherwise answer "no".')
        

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    counter = 3
    while counter * counter <= number:
        if number % counter == 0:
            return False
        counter += 2
    return True


def get_prime_round() -> tuple:
    number = random.randint(1, 1000)
    right_answer = 'yes' if is_prime(number) else 'no'
    return (str(number), right_answer)