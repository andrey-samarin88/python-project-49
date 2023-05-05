import random


def f_question():
    print('What number is missing in the progression?')


correct_answer = ''


def f_game():
    global correct_answer
    prog = []
    k = random.randint(5, 10)  # progression size
    d = random.randint(5, 10)  # progression difference
    i = 0  # progression element number
    prog.append(random.randint(5, 10))  # the first element of the progression
    u = random.randint(0, k - 1)  # the number of the unknown element of the progression
    while i < k - 1:
        prog.append(prog[i] + d)
        i += 1
    correct_answer = str(prog[u])
    prog[u] = '..'
    task = ' '.join(map(str, prog))
    print(f'Question: {task}')


def f_cor_ans() -> str:
    global correct_answer
    return correct_answer
