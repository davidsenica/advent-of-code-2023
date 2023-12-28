import os
import re

from src.advent_of_code_2023.utils import read_all, line_iterator, to_int


def solution(file_loc, prepend=False):
    result = 0
    for line in line_iterator(file_loc):
        history = [to_int(line.split())]
        while any([h != 0 for h in history[-1]]):
            history.append([history[-1][i + 1] - history[-1][i] for i in range(0, len(history[-1]) - 1)])
        tmp = 0
        for i in range(len(history) - 2, -1, -1):
            if prepend:
                tmp = history[i][0] - tmp
            else:
                tmp += history[i][-1]
        result += tmp
    return result


def first_solution(file_loc):
    return solution(file_loc)


def second_solution(file_loc):
    return solution(file_loc, prepend=True)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
