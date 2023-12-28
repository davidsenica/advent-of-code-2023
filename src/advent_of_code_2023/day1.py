import os
import re

from src.advent_of_code_2023.utils import line_iterator


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(file_loc, test_regex):
    numbers = []
    for line in line_iterator(file_loc):
        first, last = re.search(".*?(" + test_regex + ")", line), re.search(".*(" + test_regex + ")", line)
        numbers.append(int(digits.get(first.group(1), first.group(1)) + digits.get(last.group(1), last.group(1))))
    return sum(numbers)


def first_solution(file_loc):
    return solution(file_loc, "|".join(digits.values()))


def second_solution(file_loc):
    return solution(file_loc, "|".join(digits.values()) + "|" + "|".join(digits))


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
