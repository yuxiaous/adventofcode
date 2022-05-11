#!/usr/bin/env python3

input = open('day03.txt').read().strip().split('\n')


def part1(input):
    gamma = ""
    epsilon = ""

    for i in range(len(input[0])):
        bits = []
        for diagnostic in input:
            bits.append(diagnostic[i])

        if bits.count("0") > bits.count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def part2(input):
    pass


print('--- Day 3: Binary Diagnostic ---')
print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')
