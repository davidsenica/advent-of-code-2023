import os
from advent_of_code_2023.utils import line_iterator, to_int
from z3 import RealVector, Solver

def intersect(p1, p2, p3, p4):
    # copied from https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return x, y


def first_solution(file_loc):
    hailstones = []
    for line in line_iterator(file_loc):
        position, velocity = line.split(' @ ')
        hailstones.append((to_int(position.split(', ')), to_int(velocity.split(', '))))

    min_pos = []
    max_pos = []
    for hailstone in hailstones:
        min_pos.append((hailstone[0][0] + hailstone[1][0], hailstone[0][1] + hailstone[1][1]))
        max_pos.append((hailstone[0][0] + hailstone[1][0] * 4000000000000000,
                        hailstone[0][1] + hailstone[1][1] * 4000000000000000))
    result = 0
    for i in range(len(min_pos) - 1):
        for j in range(i + 1, len(min_pos)):
            intersection = intersect(min_pos[i], max_pos[i], min_pos[j], max_pos[j])
            if intersection is not None:
                if 200000000000000 <= intersection[0] <= 400000000000000 and 200000000000000 <= intersection[1] <= 400000000000000:
                    result += 1
    return result


def second_solution(file_loc):
    hailstones = []
    for line in line_iterator(file_loc):
        position, velocity = line.split(' @ ')
        hailstones.append((to_int(position.split(', ')), to_int(velocity.split(', '))))

    rock = RealVector('r', 6)
    time = RealVector('t', 3)

    s = Solver()
    for i in range(3):
        for t, hailstone in zip(time, hailstones):
            position, velocity = hailstone
            s.add(rock[i] + rock[i + 3] * t == position[i] + velocity[i] * t)
    s.check()
    return s.model().eval(sum(rock[:3]))


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
