#!/usr/bin/env python3

input = open('day09.txt').read().strip().split('\n')
input = [[int(c) for c in r] for r in input]
ROW = len(input)
COLUMN = len(input[0])


def part1(input):
    sum = 0
    for r in range(ROW):
        for c in range(COLUMN):
            lowest = True
            height = input[r][c]
            if r - 1 >= 0 and height >= input[r-1][c]:
                lowest = False
            if r + 1 < ROW and height >= input[r+1][c]:
                lowest = False
            if c - 1 >= 0 and height >= input[r][c-1]:
                lowest = False
            if c + 1 < COLUMN and height >= input[r][c+1]:
                lowest = False
            if lowest:
                risk = height + 1
                sum += risk
    return sum


def part2(input):
    def find_basin(location):
        basin = set()
        next = [location]
        while len(next) > 0:
            check = next
            next = []
            for r, c in check:
                if input[r][c] < 9:
                    basin.add((r, c))
                    if r - 1 >= 0 and (r-1, c) not in basin:
                        next.append((r-1, c))
                    if r + 1 < ROW and (r+1, c) not in basin:
                        next.append((r+1, c))
                    if c - 1 >= 0 and (r, c-1) not in basin:
                        next.append((r, c-1))
                    if c + 1 < COLUMN and (r, c+1) not in basin:
                        next.append((r, c+1))
        return basin

    basins = []
    for r in range(ROW):
        for c in range(COLUMN):
            lowest = True
            height = input[r][c]
            if r - 1 >= 0 and height >= input[r-1][c]:
                lowest = False
            if r + 1 < ROW and height >= input[r+1][c]:
                lowest = False
            if c - 1 >= 0 and height >= input[r][c-1]:
                lowest = False
            if c + 1 < COLUMN and height >= input[r][c+1]:
                lowest = False
            if lowest:
                basins.append(find_basin((r, c)))

    sizes = [len(x) for x in basins]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == '__main__':
    print('--- Day 9: Smoke Basin ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
