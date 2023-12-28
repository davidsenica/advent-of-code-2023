import math
import os

from src.advent_of_code_2023.utils import line_iterator, read_all


def parse_file(file_loc):
    content = read_all(file_loc)
    nodes = {}
    for n in content[2:]:
        n1, n2 = n.split(' = ')
        tmp = n2.split(', ')
        nodes[n1] = (tmp[0][1:], tmp[1][:-1])
    return content[0], nodes


def make_move(instruction, nodes, current_node):
    if instruction == 'L':
        return nodes[current_node][0]
    return nodes[current_node][1]


def first_solution(file_loc):
    instruction, nodes = parse_file(file_loc)
    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        current_node = make_move(instruction[steps % len(instruction)], nodes, current_node)
        steps += 1
    return steps


def second_solution(file_loc):
    instruction, nodes = parse_file(file_loc)
    solution = []
    current_nodes = [n for n in nodes.keys() if n[-1] == 'A']
    for c in current_nodes:
        steps = 0
        current_node = c
        while current_node[-1] != 'Z':
            current_node = make_move(instruction[steps % len(instruction)], nodes, current_node)
            steps += 1
        solution.append(steps)
    return math.lcm(*solution)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
