import random


def calc_game():
    question = 'What is the result of the expression?'
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    action = random.sample(['+', '-', '*'], 1)
    task = f'{number1} {action[0]} {number2}'
    correct_answer = eval(task)
    return [question, task, correct_answer]
