import prompt
import random


def even(a: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            print(f"Let's try again, {a}!")
            break
        i += 1
    if i == 3:
        print(f"'Congratulations, {a}!'")
    return
