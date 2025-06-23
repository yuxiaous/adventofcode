import os
import re

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").read()
    return lines


def mul(X, Y):
    return int(X) * int(Y)


def part1():
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    matches = re.findall(pattern, input())
    results = [mul(pairs[0], pairs[1]) for pairs in matches]
    print(sum(results))


def part2():
    sum = 0
    enable = True

    pattern = r"do\(\)|don't\(\)|mul\((-?\d+),\s*(-?\d+)\)"
    for match in re.finditer(pattern, input()):
        if match.group() == "do()":
            enable = True
        elif match.group() == "don't()":
            enable = False
        elif enable:
            pairs = match.groups()
            sum += mul(pairs[0], pairs[1])

    print(sum)


part1()
part2()
