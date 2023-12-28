import os

from advent_of_code_2023.utils import read_all, line_iterator, print_matrix


def transpose(x):
    return list(map(list, zip(*x)))


def check_for_horizontal(pattern, max_mismatches):
    result = 0
    for row in range(len(pattern) - 1):
        mismatch = 0
        for k in range(len(pattern)):
            i, j = row - k, row + 1 + k
            if 0 <= i < j < len(pattern):
                for a, b in zip(pattern[i], pattern[j]):
                    if a != b: mismatch += 1
        if mismatch == max_mismatches:
            result += row + 1
    return result

def solve(file_loc, max_mismatches=0):
    patterns = []
    current = []
    result = 0
    for line in line_iterator(file_loc):
        if len(line) == 0:
            patterns.append(current)
            current = []
            continue
        current.append([*line])
    patterns.append(current)

    for pattern in patterns:
        result += 100 * (check_for_horizontal(pattern, max_mismatches))
        result += check_for_horizontal(transpose(pattern), max_mismatches)
    return result


def first_solution(file_loc):
    return solve(file_loc)


def second_solution(file_loc):
    return solve(file_loc, 1)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
