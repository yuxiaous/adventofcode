#!/usr/bin/env python3

input = open('day11.txt').read().strip().split('\n')


class OctopuseGrid:
    def __init__(self, input):
        self.grid = [[int(c) for c in r] for r in input]
        self.row = len(self.grid)
        self.column = len(self.grid[0])
        self.total = self.row * self.column

    def gain_energy(self):
        for r in range(self.row):
            for c in range(self.column):
                self.grid[r][c] += 1

    def flash(self):
        def _flash(row, col):
            self.grid[row][col] = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r >= 0 and r < self.row and c >= 0 and c < self.column:
                        if self.grid[r][c] > 0:
                            self.grid[r][c] += 1
                            if self.grid[r][c] > 9:
                                _flash(r, c)
        for r in range(self.row):
            for c in range(self.column):
                if self.grid[r][c] > 9:
                    _flash(r, c)

        count = 0
        for r in range(self.row):
            for c in range(self.column):
                if self.grid[r][c] == 0:
                    count += 1
        return count


def part1(input):
    grid = OctopuseGrid(input)

    count = 0
    for _ in range(100):
        grid.gain_energy()
        count += grid.flash()
    return count


def part2(input):
    grid = OctopuseGrid(input)

    step = 0
    while True:
        step += 1
        grid.gain_energy()
        count = grid.flash()
        if count == grid.total:
            break
    return step


if __name__ == '__main__':
    print('--- Day 11: Dumbo Octopus ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
