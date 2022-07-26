import prompt
from brain_games.games.brain_calc import calc_get_question_and_answer
from brain_games.games.brain_gcd import gcd_get_question_and_answer
from brain_games.games.brain_even import even_get_question_and_answer
from brain_games.games.brain_progression import progression_get_question_and_answer
from brain_games.games.brain_prime import prime_get_question_and_answer


def game_start_introduction(game_name: str) -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(rules.get(game_name))
    return user_name


def game_exit(user_name: str, win: bool):
    if win:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")


def game_play(game_name: str) -> bool:
    wins = 0
    attempts = attempts_dict.get(game_name)
    while wins < 3:
        question, true_answer = get_question_and_answer(game_name)
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            wins += 1
            print('Correct!')
        else:
            attempts -= 1
            wins = 0
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
        if attempts == 0:
            return False
    return True


if __name__ == '__main__':
    pass


rules = {
    "brain-calc": 'What is the result of the expression?',
    "brain-even": 'Answer "yes" if the number is even, otherwise answer "no".',
    "brain-gcd": 'Find the greatest common divisor of given numbers.',
    "brain-progression": 'What number is missing in the progression?',
    "brain-prime": 'Answer "yes" if given number is prime. Otherwise answer "no"'
}


def get_question_and_answer(game_name):
    question_and_answer = {
        'brain-calc': calc_get_question_and_answer,
        'brain-even': even_get_question_and_answer,
        'brain-gcd': gcd_get_question_and_answer,
        'brain-progression': progression_get_question_and_answer,
        'brain-prime': prime_get_question_and_answer
    }
    return question_and_answer.get(game_name)()


attempts_dict = {
    'brain-gcd': 1,
    'brain-progression': 1,
    'brain-calc': -1,
    'brain-even': -1,
    'brain-prime': -1
}


