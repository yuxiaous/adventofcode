#!/usr/bin/env python3
import numpy as np
import math

input = open('day19.txt').read().strip()

scanners_list = []
for s in input.split('\n\n'):
    beacons_list = []
    for p in s.split('\n')[1:]:
        beacon = tuple(int(x) for x in p.split(','))
        beacons_list.append(beacon)
    scanners_list.append(beacons_list)

orientations_list = [
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
    ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
    ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
    ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
    ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
    ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
    ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
    ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
    ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
]

# make scanner list
scanners = []
for beacons_list in scanners_list:
    orientations = []
    for o in orientations_list:
        R = np.array(o)
        beacons = {}
        for b1 in beacons_list:
            vectors = set()
            for b2 in beacons_list:
                if b1 != b2:
                    vector = np.array(b2) - np.array(b1)
                    vectors.add(tuple(R @ vector))
            beacons[b1] = vectors
        orientations.append(beacons)
    scanners.append(orientations)


def match_beacons(beacons1, beacons2):
    for beacon1, vectors1 in beacons1.items():
        for beacon2, vectors2 in beacons2.items():
            same = vectors1 & vectors2
            if same and len(same) >= 11:
                return (beacon1, beacon2)


absolute_scanners = set()
absolute_beacons = {}

# move beacons of scanner 1 to absolute map
absolute_scanners.add((0, 0, 0))
for b, v in scanners[0][0].items():
    absolute_beacons[b] = v
scanners.pop(0)

# match
while len(scanners) > 0:
    for scanner in scanners.copy():
        for beacons in scanner:
            matches = match_beacons(absolute_beacons, beacons)
            if matches:
                scanners.remove(scanner)
                orientation_index = scanner.index(beacons)
                orientation_matrix = orientations_list[orientation_index]
                R = np.array(orientation_matrix)
                T = np.array(matches[0]) - R @ np.array(matches[1])

                # convert scanners coordinates
                o = tuple(R @ (0, 0, 0) + T)
                absolute_scanners.add(o)

                # convert beacons coordinates
                for b, v in beacons.items():
                    p = tuple(R @ b + T)
                    absolute_beacons[p] = v


def part1(input):
    return len(absolute_beacons)


def part2(input):
    largest = 0
    for s1 in absolute_scanners:
        for s2 in absolute_scanners:
            if s1 != s2:
                vector = tuple(np.array(s1) - np.array(s2))
                manhattan = sum([abs(x) for x in vector])
                if manhattan > largest:
                    largest = manhattan
    return largest


if __name__ == '__main__':
    print('--- Day 19: Beacon Scanner ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
