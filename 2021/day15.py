#!/usr/bin/env python3

input = open('day15.txt').read().strip().split('\n')


def find_lowest_risk_paths(risk_map):
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
            print('')
            break
    return paths


def part1(input):
    map_w = len(input[0])
    map_h = len(input)

    risk_map = {}
    for y in range(map_w):
        for x in range(map_h):
            risk_map[(x, y)] = int(input[y][x])

    paths = find_lowest_risk_paths(risk_map)
    return paths[(map_w - 1, map_h - 1)]


def part2(input):
    tile_w = len(input[0])
    tile_h = len(input)
    map_w = tile_w * 5
    map_h = tile_h * 5

    risk_map = {}
    for i in range(5):
        for j in range(5):
            for y in range(tile_h):
                for x in range(tile_w):
                    risk = int(input[y][x]) + i + j
                    while risk > 9:
                        risk -= 9
                    risk_map[(tile_w * i + x,   tile_h * j + y)] = risk

    paths = find_lowest_risk_paths(risk_map)
    return paths[(map_w - 1, map_h - 1)]


if __name__ == '__main__':
    print('--- Day 15: Chiton ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
