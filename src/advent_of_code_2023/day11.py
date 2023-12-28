import os
from advent_of_code_2023.utils import line_iterator


def manhattan_distance(start, end):
    return sum(abs(val1 - val2) for val1, val2 in zip(start, end))


def get_empty_spaces(g1, g2, rows, cols):
    num = 0
    for i in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
        if i not in rows:
            num += 1
    for j in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
        if j not in cols:
            num += 1
    return num


def solution(file_loc, empty=2):
    distances = []
    galaxies_location = []
    rows = set()
    cols = set()
    for i, line in enumerate(line_iterator(file_loc)):
        for j, cell in enumerate(line):
            if cell == '#':
                rows.add(i)
                cols.add(j)
                galaxies_location.append((i, j))

    for i in range(len(galaxies_location) - 1):
        for j in range(i + 1, len(galaxies_location)):
            num_empty = get_empty_spaces(galaxies_location[i], galaxies_location[j], rows, cols)
            distances.append(manhattan_distance(galaxies_location[i], galaxies_location[j]) + num_empty * (empty - 1))
    return sum(distances)


def first_solution(file_loc):
    return solution(file_loc)


def second_solution(file_loc):
    return solution(file_loc, empty=100000)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

