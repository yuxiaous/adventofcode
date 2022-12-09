#!/usr/bin/env python3

input = [x for x in open("day04.txt").read().strip().split("\n")]
pairs = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in input]


def part1():
    count = 0

    for pair in pairs:
        range1 = range(pair[0][0], pair[0][1] + 1)
        range2 = range(pair[1][0], pair[1][1] + 1)

        def is_fully_contain(range1, range2):
            for id in range1:
                if id not in range2:
                    return False
            return True

        if is_fully_contain(range1, range2) or is_fully_contain(range2, range1):
            count += 1

    return count


def part2():
    count = 0

    for pair in pairs:
        range1 = range(pair[0][0], pair[0][1] + 1)
        range2 = range(pair[1][0], pair[1][1] + 1)

        def is_overlap(range1, range2):
            for id in range1:
                if id in range2:
                    return True
            return False

        if is_overlap(range1, range2):
            count += 1

    return count


if __name__ == "__main__":
    print("--- Day 4: Camp Cleanup ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
