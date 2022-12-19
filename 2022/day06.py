#!/usr/bin/env python3

input = open("day06.txt").read()


def is_start_marker(marker):
    for i in range(len(marker) - 1):
        for j in range(i + 1, len(marker)):
            if marker[i] == marker[j]:
                return False
    return True


def part1():
    for i in range(4, len(input)):
        marker = input[i - 4 : i]
        if is_start_marker(marker):
            return i


def part2():
    for i in range(14, len(input)):
        marker = input[i - 14 : i]
        if is_start_marker(marker):
            return i


if __name__ == "__main__":
    print("--- Day 6: Tuning Trouble ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
