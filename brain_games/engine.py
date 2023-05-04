import prompt


def logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game.f_question()
    i = 0
    while i < 3:
        game.f_game()
        answer = prompt.string('Your answer: ')
        if answer == game.f_cor_ans():
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{game.f_cor_ans()}"')
            print(f"Let's try again, {name}!")
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')
    return
