import os
import numpy as np

from advent_of_code_2023.utils import line_iterator, print_matrix


def reachable(garden, start, total=64, is_inf=False):
    seen = set()
    positions = [(start, 0)]
    can_be_reached = set()
    while positions:
        (i, j), steps = positions.pop(0)
        if (i, j) in seen or steps > total: continue
        seen.add((i, j))
        can_be_reached.add(((i, j), steps))
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + move[0], j + move[1]
            if is_inf:
                if garden[ni % len(garden)][nj % len(garden[0])] != '#':
                    positions.append(((ni, nj), steps + 1))
            else:
                if 0 <= ni < len(garden) and 0 <= nj < len(garden[0]) and garden[ni][nj] != '#':
                    positions.append(((ni, nj), steps + 1))
    return can_be_reached


def first_solution(file_loc):
    garden = []
    start = None
    for i, line in enumerate(line_iterator(file_loc)):
        garden.append([*line])
        for j, cel in enumerate(garden[i]):
            if cel == 'S':
                start = (i, j)
                garden[i][j] = '.'
    can_be_reached = reachable(garden, start, 64)
    result = 0
    for _, steps in can_be_reached:
        if steps % 2 == 0:
            result += 1
    return result

def quad(y, n):
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * n**2) + (b * n) + c


def second_solution(file_loc):
    garden = []
    start = None
    for i, line in enumerate(line_iterator(file_loc)):
        garden.append([*line])
        for j, cel in enumerate(garden[i]):
            if cel == 'S':
                start = (i, j)
                garden[i][j] = '.'
    values = []
    for total_steps in [65, 65 + len(garden), 65 + len(garden) * 2]:
        can_be_reached = reachable(garden, start, total_steps, is_inf=True)
        tmp = 0
        for _, steps in can_be_reached:
            if steps % 2 == total_steps % 2:
                tmp += 1
        values.append(tmp)

    # quadratic formula
    n = (26501365 - 65) // len(garden)
    x1 = (values[2] - (2 * values[1]) + values[0]) // 2
    x2 = values[1] - values[0] - x1
    x3 = values[0]
    return (x1 * n ** 2) + (x2 * n) + x3


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
