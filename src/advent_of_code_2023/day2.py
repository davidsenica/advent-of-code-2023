import math
import os

from advent_of_code_2023.utils import line_iterator


def first_solution(file_loc):
    games = []
    for line in line_iterator(file_loc):
        games.append(line.split(': ')[1].split('; '))
    possible = []
    max_balls = {'red': 12, 'green': 13, 'blue': 14}
    for i, game in enumerate(games):
        is_possible = True
        for g in game:
            for balls in g.split(', '):
                num, color = balls.split(' ')
                if int(num) > max_balls[color]:
                    is_possible = False
        if is_possible:
            possible.append(i + 1)
    return sum(possible)


def second_solution(file_loc):
    games = []
    for line in line_iterator(file_loc):
        games.append(line.split(': ')[1].split('; '))
    powers = []
    for game in games:
        lowest = {'red': 0, 'green': 0, 'blue': 0}
        for g in game:
            for balls in g.split(', '):
                num, color = balls.split(' ')
                if lowest[color] < int(num):
                    lowest[color] = int(num)
        powers.append(math.prod(lowest.values()))
    return sum(powers)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

