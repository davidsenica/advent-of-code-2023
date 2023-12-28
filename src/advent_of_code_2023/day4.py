import os
import re
from copy import copy

from src.advent_of_code_2023.utils import line_iterator, to_int, read_all


def solution(file_loc):
    total_value = 0
    copies = {}

    for i, line in enumerate(line_iterator(file_loc)):
        if i not in copies:
            copies[i] = 1
        card = line.split(': ')[1]
        winning, mine = card.split('|')
        winning_num = to_int(re.sub(' +', ' ', winning.strip()).split(' '))
        mine_num = to_int(re.sub(' +', ' ', mine.strip()).split(' '))
        num_wins = len(set(winning_num) & set(mine_num))
        total_value += 2 ** (num_wins - 1) if num_wins > 0 else 0
        for j in range(i + 1, i + num_wins + 1):
            copies[j] = copies.get(j, 1) + copies[i]
    return total_value, sum(copies.values())


def first_solution(file_loc):
    return solution(file_loc)[0]


def second_solution(file_loc):
    return solution(file_loc)[1]


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
