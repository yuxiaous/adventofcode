#!/usr/bin/env python3

input = open('day08.txt').read().strip().split('\n')


def part1(input):
    count = 0
    for entry in input:
        values = entry.split('|')[1].split()
        for value in values:
            if len(value) in {2, 3, 4, 7}:
                count += 1
    return count


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 8: Seven Segment Search ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
