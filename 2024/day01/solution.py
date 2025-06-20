import os

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").readlines()
    pairs = [[int(n) for n in line.split("   ")] for line in lines]
    return list(zip(*pairs))


def part1():
    left, right = [sorted(side) for side in input()]
    distances = [abs(l-r) for l, r in zip(left, right)]
    print(sum(distances))


def part2():
    left, right = input()
    scores = [l * right.count(l) for l in left]
    print(sum(scores))


part1()
part2()
