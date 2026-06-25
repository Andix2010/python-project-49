import random

from brain_games.general_engine import run_game


def run_progression_game(name: str) -> None:
    run_game(get_progression_round, name, 
            'What number is missing in the progression?')
        

def get_progression_round() -> tuple:
    first_number = random.randint(1, 40)
    step = random.randint(1, 10)
    length = random.randint(5, 15)
    array = [str(first_number + step * i) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    right_answer = str(array[hidden_index])
    array[hidden_index] = ".."
    
    return (' '.join(array), right_answer)