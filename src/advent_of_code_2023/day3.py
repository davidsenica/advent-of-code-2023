import os
import re
import math
from collections import defaultdict
from curses.ascii import isdigit

from src.advent_of_code_2023.utils import read_all


def check_surrouding(row, j_start, j_end, engine_map):
    for i in [row - 1, row, row + 1]:
        for j in range(j_start, j_end + 1):
            if 0 <= i < len(engine_map) and 0 <= j < len(engine_map[i]):
                if not isdigit(engine_map[i][j]) and engine_map[i][j] != '.':
                    if engine_map[i][j] == '*':
                        return True, (i, j)
                    return True, None
    return False, None


def solution(file_loc):
    engine_map = read_all(file_loc)
    digit = re.compile(r'\d+')
    s = 0
    gears = defaultdict(list)
    for row in range(len(engine_map)):
        for number in re.finditer(digit, engine_map[row]):
            is_valid, gear_position = check_surrouding(row, number.start() - 1, number.end(), engine_map)
            if is_valid:
                num = int(number.group(0))
                s += num
                if gear_position is not None:
                    gears[gear_position].append(num)
    return s, gears


def first_solution(file_loc):
    result, _ = solution(file_loc)
    return result


def second_solution(file_loc):
    _, gears = solution(file_loc)
    result = 0
    for v in gears.values():
        if len(v) > 1:
            result += math.prod(v)
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
