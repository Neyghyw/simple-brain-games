import random


def progression_get_question_and_answer() -> (str, str):
    progression_step = random.randint(1, 10)
    first_num = random.randint(1, 50)
    last_num = first_num + progression_step * (10 - 1)
    question = ''
    for num in range(first_num, last_num, progression_step):
        question += f'{num} '
    progression_tuple = question.rstrip().split(' ')
    answer = random.choice(progression_tuple)
    question = question.replace(answer, "..", 1)
    return question, answer


if __name__ == "__main__":
    pass
