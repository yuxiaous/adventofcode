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


part1()
