import os
from collections import defaultdict

from advent_of_code_2023.utils import line_iterator


def custom_eval(op, val):
    if op == '<':
        return lambda n: n < val
    elif op == '>':
        return lambda n: n > val


def pars_flows(ru):
    workflows = {}
    a = ru.replace('{', ' ').replace('}', '')

    for line in a.splitlines():
        name, rules = line.split()

        rule_list = []

        for r in rules.split(','):
            if ':' in r:
                pred, dest = r.split(':')
                var = pred[0]
                op = pred[1]
                val = int(pred[2:])
                rule_list.append((dest, var, val, custom_eval(op, val)))
            else:
                rule_list.append(r)

        workflows[name] = rule_list

    return workflows


def evaluate(current, rules, x, m, a, s):
    for rule in rules[current].split(','):
        if rule == 'A':
            return True
        if rule == 'R':
            return False
        if ':' not in rule:
            return evaluate(rule, rules, x, m, a, s)
        cond, res = rule.split(':')
        if eval(cond):
            if res == "R":
                return False
            if res == "A":
                return True
            return evaluate(res, rules, x, m, a, s)


def possible(current, workflows, x, m, a, s):
    if current == 'A':
        return len(x) * len(m) * len(a) * len(s)
    if current == 'R':
        return 0
    rules = workflows[current]
    c = 0
    for r in rules:
        if isinstance(r, tuple):
            dest = r[0]
            var = r[1]
            test2 = r[3]

            if var == 'x':
                take_x = tuple(filter(test2, x))
                if len(take_x):
                    c += possible(dest, workflows, take_x, m, a, s)
                x = tuple(n for n in x if not test2(n))
            elif var == 'm':
                take_m = tuple(filter(test2, m))
                if len(take_m):
                    c += possible(dest, workflows, x, take_m, a, s)
                m = tuple(n for n in m if not test2(n))
            elif var == 'a':
                take_a = tuple(filter(test2, a))
                if len(take_a):
                    c += possible(dest, workflows, x, m, take_a, s)
                a = tuple(n for n in a if not test2(n))
            elif var == 's':
                take_s = tuple(filter(test2, s))
                if len(take_s):
                    c += possible(dest, workflows, x, m, a, take_s)
                s = tuple(n for n in s if not test2(n))
        else:
            c += possible(r, workflows, x, m, a, s)

    return c


def first_solution(file_loc):
    result = 0
    temp_rules, temp_rating = open(file_loc).read().split('\n\n')
    rules = {}
    ratings = []
    for rule in temp_rules.split('\n'):
        r, rest = rule.split('{')
        rules[r] = rest[:-1]
    for r in temp_rating.split('\n'):
        parsed = {}
        for v in r[1:-1].split(','):
            var, val = v.split('=')
            parsed[var] = int(val)
        ratings.append(parsed)
    for rating in ratings:
        if evaluate('in', rules, **rating):
            for v in rating.values():
                result += v
    return result


def second_solution(file_loc):
    temp_rules, temp_rating = open(file_loc).read().split('\n\n')
    rules = pars_flows(temp_rules)
    ratings = []
    for r in temp_rating.split('\n'):
        parsed = {}
        for v in r[1:-1].split(','):
            var, val = v.split('=')
            parsed[var] = int(val)
        ratings.append(parsed)
    return possible('in', rules, list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001)))


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
