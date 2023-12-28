import functools
import os

from advent_of_code_2023.utils import line_iterator, to_int


@functools.lru_cache(maxsize=None)
def solve(springs, arrangements, result=0):
    if len(arrangements) == 0:
        return '#' not in springs
    current, arrangements = arrangements[0], arrangements[1:]
    for i in range(len(springs) - sum(arrangements) - len(arrangements) - current + 1):
        if "#" in springs[:i]:
            break
        next_ = i + current
        if next_ <= len(springs) and '.' not in springs[i: next_] and springs[next_: next_ + 1] != "#":
            result += solve(springs[next_ + 1:], arrangements)
    return result


def first_solution(file_loc):
    result = 0
    for line in line_iterator(file_loc):
        springs, arrangements = line.split(' ')
        arrangements = tuple(to_int(arrangements.split(',')))
        result += solve(springs, arrangements)
    return result


def second_solution(file_loc):
    result = 0
    for line in line_iterator(file_loc):
        springs, arrangements = line.split(' ')
        arrangements = to_int(arrangements.split(','))
        springs = '?'.join([springs] * 5)
        arrangements = arrangements * 5
        result += solve(springs, tuple(arrangements))
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
