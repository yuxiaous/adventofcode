#!/usr/bin/env python3

input = [x for x in open("day01.txt").read().strip().split("\n\n")]
calories = [[int(c) for c in x.split("\n")] for x in input]


def part1():
    elfs = [sum(x) for x in calories]
    return max(elfs)


def part2():
    elfs = [sum(x) for x in calories]
    elfs.sort(reverse=True)
    return sum(elfs[:3])


if __name__ == "__main__":
    print("--- Day 1: Calorie Counting ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
