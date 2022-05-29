#!/usr/bin/env python3

import re

input = open('day22.txt').read().strip()


def parse_step(entry):
    reg = r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)'
    match = re.match(reg, entry)
    turn = match.group(1)
    x1 = int(match.group(2))
    x2 = int(match.group(3))
    y1 = int(match.group(4))
    y2 = int(match.group(5))
    z1 = int(match.group(6))
    z2 = int(match.group(7))
    return turn, (x1, x2), (y1, y2), (z1, z2)


def limit(val, lim):
    val_l, val_h = val
    lim_l, lim_h = lim
    if val_l > lim_h:
        return
    if val_h < lim_l:
        return
    return (max(val_l, lim_l), min(val_h, lim_h))


def part1(input: str):
    region = set()
    for entry in input.split('\n'):
        turn, range_x, range_y, range_z = parse_step(entry)
        range_x = limit(range_x, (-50, 50))
        range_y = limit(range_y, (-50, 50))
        range_z = limit(range_z, (-50, 50))

        if turn == 'on' and range_x and range_y and range_z:
            for x in range(range_x[0], range_x[1]+1):
                for y in range(range_y[0], range_y[1]+1):
                    for z in range(range_z[0], range_z[1]+1):
                        region.add((x, y, z))

        if turn == 'off' and range_x and range_y and range_z:
            for x in range(range_x[0], range_x[1]+1):
                for y in range(range_y[0], range_y[1]+1):
                    for z in range(range_z[0], range_z[1]+1):
                        if (x, y, z) in region:
                            region.remove((x, y, z))
    return len(region)


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 22: Reactor Reboot ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
