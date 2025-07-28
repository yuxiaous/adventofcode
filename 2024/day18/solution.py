import os
import sys

os.chdir(os.path.dirname(__file__))


def input(n=sys.maxsize):
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    map = {}

    for i in range(min(n, len(lines))):
        x, y = [int(c) for c in lines[i].split(",")]
        map[(x, y)] = "#"

    return map


def get_input_line(n):
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    return lines[n - 1]


def print_map(map: dict[tuple, str], w, h):
    for y in range(h):
        for x in range(w):
            print(map.get((x, y), "."), end="")
        print("")
    print("")


def part1():
    map = input(1024)
    w, h = 71, 71
    start = (0, 0)
    end = (w - 1, h - 1)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    steps = set()
    paths = set({(0, start)})
    records = {}

    while len(paths) > 0:
        step, (x, y) = paths.pop()

        if map.get((x, y), ".") == "#":
            continue

        record = records.get((x, y), -1)
        if record >= 0 and step >= record:
            continue
        records[(x, y)] = step

        if (x, y) == end:
            steps.add(step)
            continue

        for dx, dy in directions:
            if (x + dx) in range(w) and (y + dy) in range(h):
                paths.add((step + 1, (x + dx, y + dy)))

    print(min(steps) if steps else 0)


part1()


def part2():
    for i in range(1025, 9999):
        print(i, end="\r")
        map = input(i)
        w, h = 71, 71
        start = (0, 0)
        end = (w - 1, h - 1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        steps = set()
        paths = set({(0, start)})
        records = {}

        while len(paths) > 0:
            step, (x, y) = paths.pop()

            if map.get((x, y), ".") == "#":
                continue

            record = records.get((x, y), -1)
            if record >= 0 and step >= record:
                continue
            records[(x, y)] = step

            if (x, y) == end:
                steps.add(step)
                continue

            for dx, dy in directions:
                if (x + dx) in range(w) and (y + dy) in range(h):
                    paths.add((step + 1, (x + dx, y + dy)))

        if not steps:
            print(get_input_line(i))
            break


part2()
