#!/usr/bin/env python3
import numpy as np

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


def part1(input):
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
                        vectors.add(tuple(x for x in R @ vector))
                beacons[b1] = vectors
            orientations.append(beacons)
        scanners.append(orientations)

    # match
    overlaps = {b: v for b, v in scanners[0][0].items()}
    scanners.pop(0)

    def match_beacons(beacons1, beacons2):
        for beacon1, vectors1 in beacons1.items():
            for beacon2, vectors2 in beacons2.items():
                same = vectors1 & vectors2
                if same and len(same) >= 11:
                    return (beacon1, beacon2)

    while len(scanners) > 0:
        for scanner in scanners.copy():
            for beacons in scanner:
                matches = match_beacons(overlaps, beacons)
                if matches:
                    scanners.remove(scanner)
                    orientation_index = scanner.index(beacons)
                    orientation_matrix = orientations_list[orientation_index]
                    R = np.array(orientation_matrix)
                    T = np.array(matches[0]) - R @ np.array(matches[1])
                    for b, v in beacons.items():
                        p = tuple(x for x in R @ b + T)
                        overlaps[p] = v

    return len(overlaps)


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 19: Beacon Scanner ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
