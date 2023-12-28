import os
import sys
from collections import defaultdict

from advent_of_code_2023.utils import line_iterator

sys.setrecursionlimit(1000000)

def dfs(current, goal, length, seen, edges):
    if current == goal:
        return length
    seen.add(current)
    max_length = 0
    for edge in edges[current]:
        (nx, ny), v = edge
        if (nx, ny) not in seen:
            max_length = max(max_length, dfs((nx, ny), goal, length + v, seen, edges))
    seen.remove((current[0], current[1]))
    return max_length


def first_solution(file_loc):
    grid = []
    for line in line_iterator(file_loc):
        grid.append([*line])
    edges = defaultdict(set)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '#':
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (cell == '.'
                            or (cell == '>' and move == (0, 1))
                            or (cell == '<' and move == (0, -1))
                            or (cell == '^' and move == (-1, 0))
                            or (cell == 'v' and move == (1, 0))):
                        nx, ny = i + move[0], j + move[1]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            edges[(i, j)].add(((nx, ny), 1))
    return dfs((0, 1), (len(grid) - 1, len(grid[0]) - 2), 0, set(), edges)


def second_solution(file_loc):
    grid = []
    for line in line_iterator(file_loc):
        grid.append([*line])
    edges = defaultdict(set)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '#':
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = i + move[0], j + move[1]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                        edges[(i, j)].add(((nx, ny), 1))
    while True:
        for edge, values in edges.items():
            if len(values) == 2:
                (e1, v1), (e2, v2) = values
                edges[e1].remove((edge, v1))
                edges[e2].remove((edge, v2))
                edges[e1].add((e2, v1 + v2))
                edges[e2].add((e1, v1 + v2))
                del edges[edge]
                break
        else:
            break
    return dfs((0, 1), (len(grid) - 1, len(grid[0]) - 2), 0, set(), edges)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
