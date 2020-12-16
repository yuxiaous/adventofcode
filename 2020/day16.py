#!/usr/bin/env python3

import re


class Day16:
    def __init__(self, inputs):
        parts = inputs.split('\n\n')

        self.rules = {}
        for line in parts[0].split('\n'):
            match = re.match(r'(\w+\s?\w+): (\d+)-(\d+) or (\d+)-(\d+)', line)
            name = match.group(1)
            ranges = set()
            ranges.add(range(int(match.group(2)), int(match.group(3)) + 1))
            ranges.add(range(int(match.group(4)), int(match.group(5)) + 1))
            self.rules[name] = ranges

        line = parts[1].split('\n')[1]
        self.yours = [int(value) for value in line.split(',')]

        self.nearbys = []
        for line in parts[2].split('\n')[1:]:
            self.nearbys.append([int(value) for value in line.split(',')])

    def is_in_field(self, value, field):
        ranges = self.rules[field]
        for rang in ranges:
            if value in rang:
                return True
        return False

    def is_value_valid(self, value):
        for field in self.rules:
            if self.is_in_field(value, field):
                return True

    def part1(self):
        rate = 0
        for nearby in self.nearbys:
            valid = True
            for value in nearby:
                if not self.is_value_valid(value):
                    rate += value
                    valid = False
            if not valid:
                nearby.clear()
        return rate

    def part2(self):
        positions = {}
        for i in range(len(self.yours)):
            positions[i] = {
                field for field in self.rules}

        for nearby in self.nearbys:
            for i in range(len(nearby)):
                value = nearby[i]
                for field in self.rules:
                    if not self.is_in_field(value, field):
                        positions[i].remove(field)

        fields = {}
        while True:
            end = True
            for i in positions:
                if len(positions[i]) == 1:
                    end = False
                    only = next(iter(positions[i]))
                    fields[i] = only
                    for j in positions:
                        if only in positions[j]:
                            positions[j].remove(only)
                    break
            if end:
                break

        mul = 1
        for i in fields:
            if fields[i].startswith('departure'):
                mul *= self.yours[i]
        return mul


def main():
    inputs = open("day16.txt").read().strip()
    day16 = Day16(inputs)
    print(f'Part 1: {day16.part1()}')
    print(f'Part 2: {day16.part2()}')


if __name__ == "__main__":
    main()
