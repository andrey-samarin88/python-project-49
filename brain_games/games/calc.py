import random


task = ''


def f_question():
    print('What is the result of the expression?')


def f_game():
    global task
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    action = random.sample(['+', '-', '*'], 1)
    task = f'{number1} {action[0]} {number2}'
    print(f'Question: {task}')


def f_cor_ans() -> str:
    global task
    correct_answer = str(eval(task))
    return correct_answer
