#!/usr/bin/env python3

input = [int(x) for x in open('day01.txt').read().strip().split()]


def part1(input):
    increased = 0
    previous = None

    for measurement in input:
        if previous is not None:
            if measurement > previous:
                increased += 1
        previous = measurement

    return increased


def part2(input):
    increased = 0
    previous = None

    for i in range(len(input) - 2):
        measurement = sum(input[i:i+3])

        if previous is not None:
            if measurement > previous:
                increased += 1
        previous = measurement

    return increased


print("--- Day 1: Sonar Sweep ---")
print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')
