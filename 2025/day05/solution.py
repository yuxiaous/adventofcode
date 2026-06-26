import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    lists = input.split("\n\n")
    ranges = [tuple(map(int, item.split("-"))) for item in lists[0].split("\n")]
    ids = [int(item) for item in lists[1].split("\n")]
    return ranges, ids


def part1():
    ranges, ids = input()

    fresh = set()
    for id in ids:
        for lower, upper in ranges:
            if lower <= id <= upper:
                fresh.add(id)

    print("part1: ", len(fresh))


def part2():
    ranges = set(input()[0])
    merged = set()

    while ranges:
        lower1, upper1 = ranges.pop()
        for lower2, upper2 in ranges:
            if upper2 >= lower1 and lower2 <= upper1:
                lower = min(lower1, upper1, lower2, upper2)
                upper = max(lower1, upper1, lower2, upper2)

                ranges.remove((lower2, upper2))
                ranges.add((lower, upper))
                break
        else:
            merged.add((lower1, upper1))

    print("part2: ", sum([upper - lower + 1 for lower, upper in merged]))


part1()
part2()
