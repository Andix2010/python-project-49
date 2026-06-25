from brain_games.cli import welcome_user
from brain_games.games.calc_game import run_calc_game
from brain_games.greeting import greet


def main():
    greet()
    name = welcome_user()
    run_calc_game(name)


if __name__ == "__main__":
    main()