#!/usr/bin/env python3

from numpy import around


input = open('day07.txt').read().strip().split(',')
input = [int(x) for x in input]


def part1(input):
    low = min(input)
    high = max(input)
    least = None
    for pos in range(low, high+1):
        fuel = sum(abs(pos - x) for x in input)
        if least is None or least > fuel:
            least = fuel
    return least


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 7: The Treachery of Whales ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
