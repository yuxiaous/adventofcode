import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    tiles = [tuple(map(int, line.split(","))) for line in input.split("\n")]
    return tiles


def part1():
    tiles = input()

    areas = []
    for i in range(len(tiles) - 1):
        for j in range(i, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            areas.append(area)

    print("part1:", max(areas))


part1()
