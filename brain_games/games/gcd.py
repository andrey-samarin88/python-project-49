import random
import math


def f_question():
    print('Find the greatest common divisor of given numbers.')


number1 = 0
number2 = 0


def f_game():
    global number1
    global number2
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    task = f'{number1} {number2}'
    print(f'Question: {task}')


def f_cor_ans() -> str:
    global number1
    global number2
    correct_answer = str(math.gcd(number1, number2))
    return correct_answer
