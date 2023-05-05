import random


number = 0


def f_question():
    print(f'Answer "yes" if the number is even, otherwise answer "no".')


def f_game():
    global number
    number = random.randint(1, 100)
    print(f'Question: {number}')


def f_cor_ans() -> str:
    global number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
