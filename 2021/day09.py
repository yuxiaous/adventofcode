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
    pass


if __name__ == '__main__':
    print('--- Day 9: Smoke Basin ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
