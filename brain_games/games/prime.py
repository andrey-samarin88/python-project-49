import random
from math import sqrt

number = 0


def f_question():
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')


def f_game():
    global number
    number = random.randint(2, 20)
    print(f'Question: {number}')


def f_cor_ans() -> str:
    global number
    correct_answer = 'yes'
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            correct_answer = 'no'
            break
        i += 1
    return correct_answer
