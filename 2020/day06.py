#!/usr/bin/env python3

from functools import reduce


class Day6:
    def __init__(self, inputs):
        self.groups = [group for group in inputs.split('\n\n')]

    def part1(self):
        count = 0
        for group in self.groups:
            answers = reduce(lambda a, b: set(a) | set(b), group.split('\n'))
            count += len(answers)
        return count

    def part2(self):
        count = 0
        for group in self.groups:
            answers = reduce(lambda a, b: set(a) & set(b), group.split('\n'))
            count += len(answers)
        return count


def main():
    inputs = open('day06.txt').read().strip()
    day6 = Day6(inputs)
    print(f'Part 1: {day6.part1()}')
    print(f'Part 2: {day6.part2()}')


if __name__ == "__main__":
    main()
