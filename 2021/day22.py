#!/usr/bin/env python3

import re

input = open('day22.txt').read().strip()
input = input.split('\n')


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
    return turn, x1, x2, y1, y2, z1, z2


def limit(val, lim):
    v1, v2 = val
    l1, l2 = lim
    return v1 in range(l1, l2+1) and v2 in range(l1, l2+1)


def part1(input):
    region = set()
    for entry in input:
        turn, x1, x2, y1, y2, z1, z2 = parse_step(entry)

        # check range
        in_range_x = limit((x1, x2), (-50, 50))
        in_range_y = limit((y1, y2), (-50, 50))
        in_range_z = limit((z1, z2), (-50, 50))
        if not in_range_x or not in_range_y or not in_range_z:
            continue
        # turn on cubes
        if turn == 'on':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        region.add((x, y, z))
        # turn off cubes
        elif turn == 'off':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        if (x, y, z) in region:
                            region.remove((x, y, z))
    return len(region)


class Cuboid:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def intersect(self, other):
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        z1 = max(self.z1, other.z1)
        z2 = min(self.z2, other.z2)
        if x1 < x2 and y1 < y2 and z1 < z2:
            return Cuboid(x1, x2, y1, y2, z1, z2)

    def split(self, other):
        inte = self.intersect(other)
        if inte:
            return [
                Cuboid(self.x1, inte.x1, self.y1, self.y2, self.z1, self.z2),
                Cuboid(inte.x2, self.x2, self.y1, self.y2, self.z1, self.z2),
                Cuboid(inte.x1, inte.x2, self.y1, inte.y1, self.z1, self.z2),
                Cuboid(inte.x1, inte.x2, inte.y2, self.y2, self.z1, self.z2),
                Cuboid(inte.x1, inte.x2, inte.y1, inte.y2, self.z1, inte.z1),
                Cuboid(inte.x1, inte.x2, inte.y1, inte.y2, inte.z2, self.z2),
            ]
        else:
            return [
                Cuboid(self.x1, self.x2, self.y1, self.y2, self.z1, self.z2),
            ]

    def volume(self):
        len_x = self.x2-self.x1
        len_y = self.y2-self.y1
        len_z = self.z2-self.z1
        return len_x * len_y * len_z


def part2(input):
    region: list[Cuboid] = []
    for entry in input:
        turn, x1, x2, y1, y2, z1, z2 = parse_step(entry)

        cuboid = Cuboid(x1, x2+1, y1, y2+1, z1, z2+1)

        new_region = []
        for on in region:
            for chip in on.split(cuboid):
                new_region.append(chip)

        if turn == 'on':
            new_region.append(cuboid)

        region = new_region

    return sum(x.volume() for x in region)


if __name__ == '__main__':
    print('--- Day 22: Reactor Reboot ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
