#!/usr/bin/env python3

input = open('day11.txt').read().strip().split('\n')
ROW = len(input)
COLUMN = len(input[0])


def part1(input):
    grid = [[int(c) for c in r] for r in input]

    def flash(row, col):
        # flash
        grid[row][col] = 0
        # charge adjacent octopuses
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r >= 0 and r < ROW and c >= 0 and c < COLUMN:
                    if grid[r][c] > 0:
                        grid[r][c] += 1
                        if grid[r][c] > 9:
                            flash(r, c)

    count = 0
    for _ in range(100):
        for r in range(ROW):
            for c in range(COLUMN):
                grid[r][c] += 1
        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] > 9:
                    flash(r, c)
        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] == 0:
                    count += 1
    return count


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 11: Dumbo Octopus ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
