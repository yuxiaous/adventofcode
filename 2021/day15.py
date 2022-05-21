#!/usr/bin/env python3

input = open('day15.txt').read().strip().split('\n')
ROW = len(input)
COLUMN = len(input[0])


def part1(input):
    risk_map = {}
    for y in range(len(input)):
        for x in range(len(input[0])):
            risk_map[(x, y)] = int(input[y][x])

    paths = {(0, 0): 0}
    step = 0
    while True:
        step += 1
        print(f'step: {step}', end='\r')
        copy = paths.copy()
        for end in copy.keys():
            x, y = end
            for next in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if next in risk_map:
                    risk = paths[end] + risk_map[next]
                    if (next not in paths) or (paths[next] > risk):
                        paths[next] = risk
        if copy == paths:
            break
    return paths[(COLUMN-1, ROW-1)]


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 15: Chiton ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
