import os
from collections import defaultdict

from advent_of_code_2023.utils import line_iterator

# Disclaimer:
# Originaly solved with networkx but then came accross the solution from https://www.reddit.com/user/4HbQ/ and decided to implement and understand it
# Really elegant solution. Original thread:
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/ketzp94/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def first_solution(file_loc):
    graph = defaultdict(set)
    for line in line_iterator(file_loc):
        node, rest = line.split(': ')
        for n in rest.split(' '):
            graph[node].add(n)
            graph[n].add(node)
    uniq = set(graph)
    count = lambda x: len(graph[x] - uniq)

    while sum(map(count, uniq)) != 3:
        uniq.remove(max(uniq, key=count))
    return len(uniq) * len(set(graph) - uniq)


def second_solution(file_loc):
    print(file_loc)


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))

