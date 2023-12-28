import os
from collections import defaultdict
import re
from src.advent_of_code_2023.utils import read_all, line_iterator


def build_adj(pipes):
    adjacent = defaultdict(list)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pipe = [('-LF'), ('-7J'), ('|7F'), ('|LJ')]
    for i, row in enumerate(pipes):
        for j, cell in enumerate(row):
            for k, move in enumerate(moves):
                if (cell in pipe[k]
                    and 0 <= i + move[0] < len(pipes)
                    and 0 <= j + move[1] < len(row)) \
                        and pipes[i + move[0]][j + move[1]] in '-|7LJF':
                    adjacent[(i, j)].append((i + move[0], j + move[1]))
    return adjacent


def find_loop(file_loc):
    result = 0
    pipes = []
    for line in line_iterator(file_loc):
        pipes.append([*line])
    start = None
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == 'S':
                start = (i, j)
    pipes[start[0]][start[1]] = '-'  # for my case
    positions = [start]
    seen = set()
    adj = build_adj(pipes)
    while positions:
        seen.update(positions)
        next_positions = set()
        for p in positions:
            for a in adj[p]:
                if a not in seen:
                    next_positions.add(a)
        positions = list(next_positions)
        result += 1
    return result - 1, seen, pipes


def count_area(pipes):
    area = 0
    for row in pipes:
        interior = 0
        row = re.sub(r"F-*7|L-*J", "", "".join(row))
        row = re.sub(r"F-*J|L-*7", "|", row)
        for c in row:
            if c == "|":
                interior += 1
            if interior % 2 == 1 and c == ".":
                area += 1
    return area


def first_solution(file_loc):
    result, _, _ = find_loop(file_loc)
    return result


def second_solution(file_loc):
    _, loop, pipes = find_loop(file_loc)
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if (i, j) not in loop:
                pipes[i][j] = '.'
    result = count_area(pipes)
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
