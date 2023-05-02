# import random
import prompt


def logic(question, task, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    i = 0
    while i < 3:
        print(logic()task)
        answer = prompt.integer('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            break
        i += 1
    if i == 3:
        print(f"'Congratulations, {name}!'")
    return
