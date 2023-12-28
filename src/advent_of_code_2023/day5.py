import os
import re
from copy import copy

from src.advent_of_code_2023.utils import line_iterator, read_all, to_int


def parse_input(file_loc):
    with open(file_loc) as f:
        whole = f.read()
    sections = whole.split('\n\n')
    result = []
    for sec in sections[1:]:
        result.append([tuple(to_int(line.split(' '))) for line in sec.split('\n')[1:]])

    return to_int(sections[0].split(': ')[1].split(' ')), result


def intersect(istart, iend, jstart, jend):
    return not (iend < jstart or jend < istart)


def first_solution(file_loc):
    result = []
    seeds, sections = parse_input(file_loc)
    for seed in seeds:
        orig = seed
        for section in sections:
            for mapping in section:
                dest, start, r = mapping
                if start <= orig <= start + r:
                    orig = dest + orig - start
                    break
        result.append(orig)
    return min(result)


def second_solution(file_loc):
    result = []
    seeds, sections = parse_input(file_loc)
    seeds = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
    for seed in seeds:
        new_ = [seed]
        for section in sections:
            cuts = []
            intervals = copy(new_)
            while len(intervals) > 0:
                interval = intervals.pop()
                splited = False
                for mapping in section:
                    dest, start, r = mapping
                    end = start + r
                    if intersect(interval[0], interval[1], start, end):
                        splited = True
                        c1 = max(start, interval[0])
                        c2 = min(end, interval[1])
                        cuts.append((c1 + dest - start, c2 + dest - start))
                        if interval[0] < c1:
                            intervals.append((interval[0], c1 - 1))
                        if interval[1] > c2:
                            intervals.append((c2 + 1, interval[1]))
                if not splited:
                    cuts.append(interval)
            new_ = copy(cuts)
        result += new_
    return min([r[0] for r in result])


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

