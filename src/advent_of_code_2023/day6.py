import math
import os
import re
import time

from src.advent_of_code_2023.utils import line_iterator, read_all, to_int


def first_solution(file_loc):
    result = []
    lines = read_all(file_loc)
    times, distances = to_int(lines[0].split()[1:]), to_int(lines[1].split()[1:])
    for time, distance in zip(times, distances):
        total = 0
        for i in range(time):
            if i * (time - i) > distance:
                total += 1
        result.append(total)
    return math.prod(result)


def second_solution(file_loc):
    result = 0
    lines = read_all(file_loc)
    times = to_int(lines[0].split()[1:])
    distances = to_int(lines[1].split()[1:])
    time = int("".join(str(t) for t in times))
    distance = int("".join(str(t) for t in distances))
    for i in range(time):
        if i * (time - i) > distance:
            result += 1
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
