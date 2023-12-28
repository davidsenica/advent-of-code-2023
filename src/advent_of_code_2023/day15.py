import os
from collections import defaultdict, OrderedDict


def hash_alg(chars):
    temp_result = 0
    for char in chars:
        temp_result += ord(char)
        temp_result *= 17
        temp_result %= 256
    return temp_result


def first_solution(file_loc):
    return sum(hash_alg(value) for value in open(file_loc, 'r').read().strip().split(','))


def second_solution(file_loc):
    content = open(file_loc, 'r').read().strip()
    boxes = defaultdict(OrderedDict)
    for value in content.split(','):
        if value.endswith('-'):
            label = value[:-1]
            h = hash_alg(label)
            boxes[h].pop(label, None)
        else:
            label = value[:-2]
            h = hash_alg(label)
            boxes[h][label] = int(value[-1])
    result = 0
    for b, box in boxes.items():
        for j, l in enumerate(box.values()):
            result += (1 + b) * (1 + j) * l
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

