import os
import sys

os.chdir(os.path.dirname(__file__))


def input(n=sys.maxsize):
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    w, h = 0, 0
    map = {}

    for i in range(min(n, len(lines))):
        x, y = [int(c) for c in lines[i].split(",")]
        w = max(x + 1, w)
        h = max(y + 1, h)
        map[(x, y)] = "#"

    for y in range(h):
        for x in range(w):
            if not map.get((x, y)):
                map[(x, y)] = "."

    return map, w, h


def print_map(map: dict[tuple, str], w, h):
    for y in range(h):
        for x in range(w):
            print(map[(x, y)], end="")
        print("")
    print("")


def part1():
    map, w, h = input(1024)
    start = (0, 0)
    end = (w - 1, h - 1)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    steps = set()
    paths = set({(0, start)})
    records = {}

    while len(paths) > 0:
        step, (x, y) = paths.pop()

        if map.get((x, y), "#") == "#":
            continue

        record = records.get((x, y), -1)
        if record >= 0 and step >= record:
            continue
        records[(x, y)] = step

        if (x, y) == end:
            steps.add(step)
            continue

        for dx, dy in directions:
            paths.add((step + 1, (x + dx, y + dy)))

    print(min(steps))


part1()
