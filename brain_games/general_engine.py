import prompt

from brain_games.check_answer import check_answer


def run_game(get_round: tuple, name: str, description: str) -> None:
    print(description)
    right_answer_count = 0

    while right_answer_count < 3:
        question, right_answer = get_round()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if not check_answer(answer, right_answer, name):
            return 
        right_answer_count += 1

    print(f"Congratulations, {name}!")
