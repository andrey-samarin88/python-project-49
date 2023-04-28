#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_even import even


def main():
    print('Welcome to the Ass Games!')
    a = welcome_user()
    even(a)


if __name__ == '__main__':
    main()
