#!/bin/bash

cat > "src/advent_of_code_2023/${1}.py" <<EOL
import os


def first_solution(file_loc):
    print(file_loc)


def second_solution(file_loc):
    print(file_loc)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

EOL