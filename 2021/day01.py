#!/usr/bin/env python3

input = open('day01.txt').read().strip().split()

def part1(input):
    increased = 0
    previous = None

    for measurement in input:
        if previous is not None:
            if measurement > previous:
                increased += 1
        previous = measurement

    return increased

print("--- Day 1: Sonar Sweep ---")
print(f'Part 1: {part1(input)}')
