def check_answer(answer: str, right_answer: str, name: str) -> bool:
    if answer == right_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'.\n"
            f"Let's try again, {name}!")
        return False