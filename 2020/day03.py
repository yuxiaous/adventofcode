#!/usr/bin/env python3

from functools import reduce


class Map:
    def __init__(self, inputs):
        self.marks = {}

        self.grids = []
        for line in inputs.split('\n'):
            row = []
            for grid in line:
                row.append(grid)
            self.grids.append(row)

    def getSize(self):
        w = len(self.grids[0])
        h = len(self.grids)
        return w, h

    def mark(self, x, y):
        grid = self.grids[y][x]
        if grid == '.':
            self.marks[(x, y)] = 'O'
        elif grid == '#':
            self.marks[(x, y)] = 'X'

    def clean(self):
        self.marks = {}

    def display(self):
        for y in range(len(self.grids)):
            row = self.grids[y]
            for x in range(len(row)):
                if (x, y) in self.marks:
                    grid = self.marks[(x, y)]
                else:
                    grid = row[x]
                print(grid, end='')
            print('')


class Day3:
    def __init__(self, inputs):
        self.map = Map(inputs)

    def encounter(self, offset):
        self.map.clean()
        x, y = 0, 0
        w, h = self.map.getSize()
        while True:
            self.map.mark(x, y)

            x += offset[0]
            y += offset[1]
            if x >= w:
                x -= w
            if y >= h:
                break

        return list(self.map.marks.values()).count('X')

    def part1(self):
        offset = (3, 1)
        return self.encounter(offset)

    def part2(self):
        offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees = [self.encounter(offset) for offset in offsets]
        return reduce(lambda a, b: a * b, trees)


def main():
    inputs = open('day03.txt').read().strip()
    day3 = Day3(inputs)
    print(f'Part 1: {day3.part1()}')
    print(f'Part 2: {day3.part2()}')


if __name__ == "__main__":
    main()
