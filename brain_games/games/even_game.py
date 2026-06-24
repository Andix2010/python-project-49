import prompt
import random


def run_even_game(name):
    right_answer_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while right_answer_count < 3:
        number = random.randint(1, 99)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        right_answer = 'yes' if (number % 2 == 0) else 'no'
        if answer == right_answer:
            print("Correct!")
            right_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'.\n"
                f"Let's try again, {name}!")
            return 
    print(f"Congratulations, {name}!")
    return