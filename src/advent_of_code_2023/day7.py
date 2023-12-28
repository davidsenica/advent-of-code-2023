import os
from curses.ascii import isdigit
from collections import Counter
from functools import cmp_to_key
from src.advent_of_code_2023.utils import read_all, line_iterator


def card_value(card, part2=False):
    if isdigit(card):
        return int(card)
    elif card == 'J':
        if part2:
            return 1
        else:
            return 11
    elif card == 'T':
        return 10
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14


def hand_value(hand):
    count = Counter(hand)
    if len(count) == 5: return 1
    if len(count) == 4: return 2
    if len(count) == 3:
        if max(count.values()) == 2:
            return 3
        else:
            return 4
    if len(count) == 2:
        if max(count.values()) == 3:
            return 5
        else:
            return 6
    return 7


def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    value1 = hand_value(hand1)
    value2 = hand_value(hand2)
    if value1 == value2:
        for i in range(len(hand1)):
            if card_value(hand1[i]) > card_value(hand2[i]):
                return 1
            elif card_value(hand1[i]) < card_value(hand2[i]):
                return -1
    if value1 > value2:
        return 1
    return -1


def compare_2(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    value1 = max([hand_value(hand1.replace('J', r)) for r in '23456789TJQKA'])
    value2 = max([hand_value(hand2.replace('J', r)) for r in '23456789TJQKA'])
    if value1 == value2:
        for i in range(len(hand1)):
            if card_value(hand1[i], True) > card_value(hand2[i], True):
                return 1
            elif card_value(hand1[i], True) < card_value(hand2[i], True):
                return -1
    if value1 > value2:
        return 1
    return -1


def first_solution(file_loc):
    hands = [line.split() for line in line_iterator(file_loc)]
    compare_key = cmp_to_key(compare)
    hands.sort(key=compare_key)
    result = 0
    for i, h in enumerate(hands):
        result += (i + 1) * int(h[1])
    return result


def second_solution(file_loc):
    hands = [line.split() for line in line_iterator(file_loc)]
    compare_key = cmp_to_key(compare_2)
    hands.sort(key=compare_key)
    result = 0
    for i, h in enumerate(hands):
        result += (i + 1) * int(h[1])
    return result


if __name__ == '__main__':
    file_loc = f'data/{os.path.basename(__file__).replace(".py", "")}/input.txt'
    print('Solution 1: ', first_solution(file_loc))
    print('Solution 2: ', second_solution(file_loc))
