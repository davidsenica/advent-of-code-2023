import os
from collections import defaultdict
from copy import deepcopy

from advent_of_code_2023.utils import line_iterator, to_int


class Brick:
    def __init__(self, positions, _id):
        self.id = _id
        self.positions = positions
        self.occupancy = set(self._calculate_occupancy())

    def _calculate_occupancy(self):
        for x in range(self.positions[0], self.positions[3] + 1):
            for y in range(self.positions[1], self.positions[4] + 1):
                for z in range(self.positions[2], self.positions[5] + 1):
                    yield x, y, z

    def fall(self, occupied):
        while True:
            self.positions[2] -= 1
            self.positions[5] -= 1
            if not any(position in occupied for position in self._calculate_occupancy()) and self.positions[2] > 0:
                continue
            else:
                self.positions[2] += 1
                self.positions[5] += 1
                self.occupancy = set(self._calculate_occupancy())
                break

    def below(self):
        for x in range(self.positions[0], self.positions[3] + 1):
            for y in range(self.positions[1], self.positions[4] + 1):
                for z in range(self.positions[2] - 1, self.positions[5]):
                    yield x, y, z

    def __hash__(self):
        return hash((tuple(self.positions), self.id))


def dependencies(bricks, occupied):
    above, below = defaultdict(set), defaultdict(set)
    for brick in bricks:
        for pos in brick.below():
            if pos in occupied and pos not in brick.occupancy:
                above[occupied[pos]].add(brick)
                below[brick].add(occupied[pos])
    return above, below


def disintegrate(brick, above, below, falling):
    if brick in falling:
        return
    falling.add(brick)
    for parent in above[brick]:
        if not len(below[parent] - falling):
            disintegrate(parent, above, below, falling)


def solve(file_loc):
    falling_bricks = []
    for i, line in enumerate(line_iterator(file_loc)):
        falling_bricks.append(Brick(to_int(line.replace('~', ',').split(',')), i))
    falling_bricks.sort(key=lambda x: x.positions[2])
    occupied = {}
    for brick in falling_bricks:
        brick.fall(occupied)
        for pos in brick.occupancy:
            occupied[pos] = brick
    above, below = dependencies(falling_bricks, occupied)
    for brick in falling_bricks:
        falling = set()
        disintegrate(brick, above, below, falling)
        yield len(falling) - 1


def first_solution(file_loc):
    result = 0
    for res in solve(file_loc):
        result += res == 0
    return result


def second_solution(file_loc):
    return sum(solve(file_loc))


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
