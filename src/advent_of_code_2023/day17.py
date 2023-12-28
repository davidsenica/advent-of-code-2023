import os
from queue import PriorityQueue

from advent_of_code_2023.utils import line_iterator, to_int


directions = {
    'up': {'left': (0, -1), 'right': (0, 1)},
    'down': {'left': (0, -1), 'right': (0, 1)},
    'left': {'up': (-1, 0), 'down': (1, 0)},
    'right': {'up': (-1, 0), 'down': (1, 0)},
    'start': {'right': (0, 1), 'down': (1, 0)}
}


def solve(heat_map, min_moves, max_moves):
    seen = set()
    costs = {}
    start = (0, (0, 0), 'start')
    positions = PriorityQueue()
    positions.put(start)
    while True:
        heat_level, current_pos, direction = positions.get()
        if current_pos[0] == len(heat_map) - 1 and current_pos[1] == len(heat_map[0]) - 1:
            return heat_level
        if (current_pos, direction) in seen:
            continue
        seen.add((current_pos, direction))

        for d, v in directions[direction].items():
            cost_increase = 0
            for i in range(1, max_moves+1):
                new_pos = (current_pos[0] + v[0] * i, current_pos[1] + v[1] * i)
                if 0 <= new_pos[0] < len(heat_map) and 0 <= new_pos[1] < len(heat_map[0]):
                    cost_increase += heat_map[new_pos[0]][new_pos[1]]
                    new_cost = heat_level + cost_increase
                    old_cost = costs.get((new_pos, d), 1e1000)
                    if new_cost < old_cost and min_moves <= i:
                        costs[(new_pos, d)] = new_cost
                        positions.put((
                            new_cost,
                            new_pos,
                            d
                        ))


def first_solution(file_loc):
    heat_map = []
    for line in line_iterator(file_loc):
        heat_map.append(to_int([*line]))
    return solve(heat_map, 1, 3)


def second_solution(file_loc):
    heat_map = []
    for line in line_iterator(file_loc):
        heat_map.append(to_int([*line]))
    return solve(heat_map, 4, 10)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

