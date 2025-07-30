import os
from typing import Dict

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    map = [[t for t in l] for l in input.split("\n")]
    return map


def print_map(map):
    h = len(map)
    w = len(map[0])
    for y in range(h):
        for x in range(w):
            print(map[y][x], end="")
        print("")
    print("")


def find_tile(map, tile):
    h, w = len(map), len(map[0])
    for y in range(h):
        for x in range(w):
            if map[y][x] == tile:
                return (x, y)


def part1():
    map = input()
    h, w = len(map), len(map[0])
    start = find_tile(map, "S")
    end = find_tile(map, "E")
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    tracks = set({(0, start)})
    cheaters = {}
    records = {}

    while len(tracks) > 0:
        time, (x, y) = tracks.pop()

        record = records.get((x, y), -1)
        if record >= 0 and time >= record:
            continue
        records[(x, y)] = time

        if (x, y) == end:
            continue

        for dx, dy in directions:
            if (
                (x + dx) in range(w)
                and (y + dy) in range(h)
                and map[y + dy][x + dx] != "#"
            ):
                tracks.add((time + 1, (x + dx, y + dy)))

        # cheaters
        for dx1, dy1 in directions:
            for dx2, dy2 in directions:
                if (
                    (x + dx1 + dx2) in range(w)
                    and (y + dy1 + dy2) in range(h)
                    and map[y + dy1 + dy2][x + dx1 + dx2] != "#"
                ):
                    cheaters[(x, y, dx1 + dx2, dy1 + dy2)] = time + 2

    saves = {}
    for (x, y, dx, dy), time in cheaters.items():
        save = records[(x + dx, y + dy)] - time
        if save <= 0:
            continue
        if save not in saves:
            saves[save] = 0
        saves[save] += 1

    count = 0
    for save, cheats in saves.items():
        if save >= 100:
            count += cheats
    print(count)


part1()


def part2():
    map = input()
    h, w = len(map), len(map[0])
    start = find_tile(map, "S")
    end = find_tile(map, "E")
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    tracks = set({(0, start)})
    cheaters = {}
    records = {}

    while len(tracks) > 0:
        time, (x, y) = tracks.pop()

        record = records.get((x, y), -1)
        if record >= 0 and time >= record:
            continue
        records[(x, y)] = time

        if (x, y) == end:
            continue

        for dx, dy in directions:
            if (
                (x + dx) in range(w)
                and (y + dy) in range(h)
                and map[y + dy][x + dx] != "#"
            ):
                tracks.add((time + 1, (x + dx, y + dy)))

        # cheaters
        most = 20
        for dx in range(-most, most + 1):
            for dy in range(-most, most + 1):
                if (
                    abs(dx) + abs(dy) <= most
                    and (x + dx) in range(w)
                    and (y + dy) in range(h)
                    and map[y + dy][x + dx] != "#"
                ):
                    cheaters[(x, y, dx, dy)] = time + abs(dx) + abs(dy)

    saves = {}
    for (x, y, dx, dy), time in cheaters.items():
        save = records[(x + dx, y + dy)] - time
        if save <= 0:
            continue
        if save not in saves:
            saves[save] = 0
        saves[save] += 1

    count = 0
    for save, cheats in saves.items():
        if save >= 100:
            count += cheats
    print(count)


part2()
