#!/usr/bin/env python3


from brain_games.engine import logic
from brain_games.games.calc import calc_game


def main():
    logic(*calc_game())


if __name__ == '__main__':
    main()
