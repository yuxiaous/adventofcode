#!/usr/bin/env python3

input = open('day25.txt').read().strip()
input = input.split('\n')


def part1(input):
    height = len(input)
    width = len(input[0])

    # make situation map
    situation_map = {}
    for y in range(height):
        for x in range(width):
            what = input[y][x]
            if what in ['>', 'v']:
                situation_map[(x, y)] = what

    step = 0
    last_situation_map = {}
    while situation_map != last_situation_map:
        last_situation_map = situation_map

        # the east-facing herd moves
        temp_situation_map = {}
        for location, seacucumber in last_situation_map.items():
            if seacucumber == '>':
                x, y = location
                x += 1
                if x >= width:
                    x -= width
                if (x, y) not in last_situation_map:
                    temp_situation_map[(x, y)] = seacucumber
                    continue
            temp_situation_map[location] = seacucumber

        # the south-facing herd moves
        situation_map = {}
        for location, seacucumber in temp_situation_map.items():
            if seacucumber == 'v':
                x, y = location
                y += 1
                if y >= height:
                    y -= height
                if (x, y) not in temp_situation_map:
                    situation_map[(x, y)] = seacucumber
                    continue
            situation_map[location] = seacucumber

        step += 1
    return step


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 25: Sea Cucumber ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
