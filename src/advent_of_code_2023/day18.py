import os

from advent_of_code_2023.utils import line_iterator, print_matrix


moves = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}


def shoelace_formula(points):
    num_points = len(points)
    s1, s2 = 0, 0
    for i in range(num_points - 1):
        s2 = s2 + points[i][0] * points[i + 1][1]
        s1 = s1 + points[i][1] * points[i + 1][0]
    s2 = s2 + points[num_points - 1][0] * points[0][1]
    s1 = s1 + points[0][0] * points[num_points - 1][1]
    return abs(s1 - s2) // 2


def convert_hex(hex):
    if hex[-1] == '0':
        return 'R', int(hex[1:-1], 16)
    if hex[-1] == '1':
        return 'D', int(hex[1:-1], 16)
    if hex[-1] == '2':
        return 'L', int(hex[1:-1], 16)
    if hex[-1] == '3':
        return 'U', int(hex[1:-1], 16)


def first_solution(file_loc):
    dig_plan = []
    vertices = []
    for line in line_iterator(file_loc):
        direction, length, color = line.split(' ')
        dig_plan.append((direction, int(length)))
    current = (0, 0)
    vertices.append(current)
    total_points = 1
    for dig in dig_plan:
        move = moves[dig[0]]
        next_vertex = (current[0] + move[0] * dig[1], current[1] + move[1] * dig[1])
        vertices.append(next_vertex)
        total_points += dig[1]
        current = next_vertex

    area = shoelace_formula(vertices)
    return area - total_points // 2 + total_points


def second_solution(file_loc):
    dig_plan = []
    vertices = []
    for line in line_iterator(file_loc):
        direction, length, color = line.split(' ')
        direction, length = convert_hex(color[1:-1])
        dig_plan.append((direction, int(length)))
    current = (0, 0)
    vertices.append(current)
    total_points = 1
    for dig in dig_plan:
        move = moves[dig[0]]
        next_vertex = (current[0] + move[0] * dig[1], current[1] + move[1] * dig[1])
        vertices.append(next_vertex)
        total_points += dig[1]
        current = next_vertex

    area = shoelace_formula(vertices)
    return area - total_points // 2 + total_points


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

