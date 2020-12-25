#!/usr/bin/env python3

import re


class Floor:
    def __init__(self):
        self.reference = (0, 0)
        self.blacks = set()

    def install(self, instruction):
        def move(pos, direction):
            if direction == 'e':
                return (pos[0] + 2, pos[1])
            elif direction == 'se':
                return (pos[0] + 1, pos[1] - 1)
            elif direction == 'sw':
                return (pos[0] - 1, pos[1] - 1)
            elif direction == 'w':
                return (pos[0] - 2, pos[1])
            elif direction == 'nw':
                return (pos[0] - 1, pos[1] + 1)
            elif direction == 'ne':
                return (pos[0] + 1, pos[1] + 1)

        current = self.reference
        for direction in instruction:
            current = move(current, direction)
        if current in self.blacks:
            self.blacks.remove(current)
        else:
            self.blacks.add(current)

    def flip(self):
        def neighbors(pos):
            adjacent = set()
            adjacent.add((pos[0] + 2, pos[1]))
            adjacent.add((pos[0] - 2, pos[1]))
            adjacent.add((pos[0] + 1, pos[1] - 1))
            adjacent.add((pos[0] - 1, pos[1] - 1))
            adjacent.add((pos[0] - 1, pos[1] + 1))
            adjacent.add((pos[0] + 1, pos[1] + 1))
            return adjacent

        checks = set()
        for pos in self.blacks:
            checks.add(pos)
            checks.update(neighbors(pos))

        flips = set()
        for pos in checks:
            count = len([x for x in neighbors(pos) if x in self.blacks])
            if pos in self.blacks:
                if count == 0 or count > 2:
                    flips.add(pos)
            else:
                if count == 2:
                    flips.add(pos)

        for pos in flips:
            if pos in self.blacks:
                self.blacks.remove(pos)
            else:
                self.blacks.add(pos)


class Day24:
    def __init__(self, inputs):
        self.instructions = [re.findall(r'e|se|sw|w|nw|ne', line)
                             for line in inputs.split('\n')]
        self.floor = Floor()

    def part1(self):
        for instruction in self.instructions:
            self.floor.install(instruction)
        return len(self.floor.blacks)

    def part2(self):
        day = 100
        for i in range(day):
            print(f'{i}/{day}', end='\r')
            self.floor.flip()
        return len(self.floor.blacks)


def main():
    inputs = open("day24.txt").read().strip()
    day24 = Day24(inputs)
    print(f'Part 1: {day24.part1()}')
    print(f'Part 2: {day24.part2()}')


if __name__ == "__main__":
    main()
