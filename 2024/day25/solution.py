import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    schematics = input.split("\n\n")

    locks = set()
    keys = set()

    for schematic in schematics:
        rows = schematic.split("\n")

        heights = [0] * 5
        for x in range(5):
            for y in range(5):
                if rows[y + 1][x] == "#":
                    heights[x] += 1

        if rows[0] == "#####":
            locks.add(tuple(heights))
        elif rows[-1] == "#####":
            keys.add(tuple(heights))

    return locks, keys


def part1():
    locks, keys = input()

    count = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock[i] + key[i] > 5:
                    break
            else:
                count += 1
    print(count)


part1()
