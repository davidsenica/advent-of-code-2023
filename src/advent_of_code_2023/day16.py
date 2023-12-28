import os

from advent_of_code_2023.utils import line_iterator

position_to_move = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

direction_change = {
    '.': {'right': 'right', 'left': 'left', 'up': 'up', 'down': 'down'},
    '|': {'right': 'up,down', 'left': 'up,down', 'up': 'up', 'down': 'down'},
    '-': {'right': 'right', 'left': 'left', 'up': 'right,left', 'down': 'right,left'},
    '/': {'right': 'up', 'left': 'down', 'up': 'right', 'down': 'left'},
    '\\': {'right': 'down', 'left': 'up', 'up': 'left', 'down': 'right'}
}


def energize(mirrors, start):
    positions = [start]
    seen = set()
    while len(positions) > 0:
        current = positions.pop(0)
        if current in seen: continue
        (i, j), direction = current
        if 0 <= i < len(mirrors) and 0 <= j < len(mirrors[0]):
            seen.add(current)
        else:
            continue
        direction = direction_change[mirrors[i][j]][direction]
        for d in direction.split(','):
            y, x = position_to_move[d]
            positions.append(((i + y, j + x), d))
    return len(set([pos for pos, dir in seen]))


def first_solution(file_loc):
    mirrors = []
    for line in line_iterator(file_loc):
        mirrors.append([*line])
    return energize(mirrors, ((0, 0), 'right'))


def second_solution(file_loc):
    mirrors = []
    results = []
    starts = []
    for line in line_iterator(file_loc):
        mirrors.append([*line])
    for x in range(len(mirrors)):
        starts.append(((x, 0), 'right'))
        starts.append(((x, len(mirrors[0]) - 1), 'left'))
    for y in range(len(mirrors[0])):
        starts.append(((0, y), 'down'))
        starts.append(((0, len(mirrors) - 1), 'up'))
    for start in starts:
        results.append(energize(mirrors, start))
    return max(results)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

