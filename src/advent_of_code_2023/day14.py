import os

from advent_of_code_2023.utils import read_all, line_iterator, print_matrix
from tqdm import trange


def tilt(rocks):
    for j, column in enumerate(rocks[0]):
        for i, row in enumerate(rocks):
            if rocks[i][j] == 'O':
                k = i - 1
                while rocks[k][j] == '.' and k >= 0:
                    rocks[k+1][j] = '.'
                    rocks[k][j] = 'O'
                    k -= 1
    return rocks

def tilt_cycle(rocks):
    for j, column in enumerate(rocks[0]):
        for i, row in enumerate(rocks):
            if rocks[i][j] == 'O':
                k = i - 1
                while rocks[k][j] == '.' and k >= 0:
                    rocks[k+1][j] = '.'
                    rocks[k][j] = 'O'
                    k -= 1
    for i, row in enumerate(rocks):
        for j, column in enumerate(rocks[0]):
                if rocks[i][j] == 'O':
                    k = j - 1
                    while rocks[i][k] == '.' and k >= 0:
                        rocks[i][k+1] = '.'
                        rocks[i][k] = 'O'
                        k -= 1
    for j, column in enumerate(rocks[0]):
        for i in range(len(rocks) - 1, -1, -1):
            if rocks[i][j] == 'O':
                k = i + 1
                while k < len(rocks) and rocks[k][j] == '.':
                    rocks[k-1][j] = '.'
                    rocks[k][j] = 'O'
                    k += 1
    for i, row in enumerate(rocks):
        for j in range(len(rocks[0]) - 1, -1, -1):
            if rocks[i][j] == 'O':
                k = j + 1
                while k < len(rocks[0]) and rocks[i][k] == '.':
                    rocks[i][k - 1] = '.'
                    rocks[i][k] = 'O'
                    k += 1
    return rocks


def calculate_load(rocks):
    load = 0
    for i, row in enumerate(rocks):
        for j, col in enumerate(row):
            if col == 'O':
                load += len(rocks) - i
    return load


def first_solution(file_loc):
    rocks = []
    for line in line_iterator(file_loc):
        rocks.append([*line])
    rocks = tilt(rocks)
    return calculate_load(rocks)


def second_solution(file_loc):
    rocks = []
    for line in line_iterator(file_loc):
        rocks.append([*line])
    memory = {}
    cycle_index = 1
    max_cycles = 1000000000
    while cycle_index <= max_cycles:
        rocks = tilt_cycle(rocks)
        rocks_str = "".join(["".join(rocks[i]) for i in range(len(rocks))])
        if rocks_str in memory:
            cycle_len = cycle_index - memory[rocks_str][0]
            for index, value in memory.values():
                if index >= memory[rocks_str][0] and index % cycle_len == max_cycles % cycle_len:
                    return value
        memory[rocks_str] = (cycle_index, calculate_load(rocks))
        cycle_index += 1



if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

