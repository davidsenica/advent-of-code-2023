import math
import os
from collections import defaultdict

from advent_of_code_2023.utils import line_iterator


def first_solution(file_loc):
    modules = {}
    switches = defaultdict(int)
    conjunction = defaultdict(dict)
    for line in line_iterator(file_loc):
        s, m = line.split(' -> ')
        if '%' in s or '&' in s:
            modules[s[1:]] = (s[0], m.split(', '))
            for tmp in m.split(', '):
                conjunction[tmp][s[1:]] = 0
        else:
            modules[s] = (None, m.split(', '))
    counts = [0, 0]
    for _ in range(1000):
        q = [('button', 'broadcaster', 0)]
        while len(q) > 0:
            from_module, module, state = q.pop(0)
            counts[state] += 1
            if module not in modules:
                continue
            module_type, next_modules = modules[module]
            match module_type, state:
                case '%', 0:
                    next_state = switches[module] = not switches[module]
                case '&', _:
                    conjunction[module][from_module] = state
                    next_state = not all(conjunction[module].values())
                case None, _:
                    next_state = state
                case _, _:
                    continue
            for n in next_modules:
                q.append((module, n, int(next_state)))
    return math.prod(counts)


def second_solution(file_loc):
    modules = {}
    switches = defaultdict(int)
    conjunction = defaultdict(dict)
    for line in line_iterator(file_loc):
        s, m = line.split(' -> ')
        if '%' in s or '&' in s:
            modules[s[1:]] = (s[0], m.split(', '))
            for tmp in m.split(', '):
                conjunction[tmp][s[1:]] = 0
                if tmp == 'rx':
                    rx = s[1:]
        else:
            modules[s] = (None, m.split(', '))
    rx_ins = {i: 0 for i in conjunction[rx]}
    counts = [0, 0]
    for i in range(100000000):
        if all(rx_ins.values()):
            return math.prod(rx_ins.values())
        q = [('button', 'broadcaster', 0)]
        while len(q) > 0:
            from_module, module, state = q.pop(0)
            counts[state] += 1
            if module not in modules:
                continue
            module_type, next_modules = modules[module]
            match module_type, state:
                case '%', 0:
                    next_state = switches[module] = not switches[module]
                case '&', _:
                    conjunction[module][from_module] = state
                    next_state = not all(conjunction[module].values())
                    if 'rx' in next_modules:
                        for k, v in conjunction[module].items():
                            if v: rx_ins[k] = i + 1
                case None, _:
                    next_state = state
                case _, _:
                    continue
            for n in next_modules:
                q.append((module, n, int(next_state)))
    return math.prod(counts)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

