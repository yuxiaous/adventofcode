import os
from turtle import pos
from typing import Dict

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").read().strip().split("\n")
    w, h = len(lines[0]), len(lines)

    antennas: Dict[str, list] = {}
    for y in range(h):
        for x in range(w):
            grid = lines[y][x]
            if grid == ".":
                continue
            if grid not in antennas:
                antennas[grid] = []
            antennas[grid].append((x, y))
    return antennas, w, h


def part1():
    antinodes = set()

    antennas, w, h = input()
    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x = positions[i][0] + positions[i][0] - positions[j][0]
                y = positions[i][1] + positions[i][1] - positions[j][1]
                if x >= 0 and x < w and y >= 0 and y < h:
                    antinodes.add((x, y))

                x = positions[j][0] + positions[j][0] - positions[i][0]
                y = positions[j][1] + positions[j][1] - positions[i][1]
                if x >= 0 and x < w and y >= 0 and y < h:
                    antinodes.add((x, y))

    print(len(antinodes))


def part2():
    antinodes = set()

    antennas, w, h = input()
    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x = positions[i][0]
                y = positions[i][1]
                dx = positions[i][0] - positions[j][0]
                dy = positions[i][1] - positions[j][1]
                while x >= 0 and x < w and y >= 0 and y < h:
                    antinodes.add((x, y))
                    x += dx
                    y += dy

                x = positions[j][0]
                y = positions[j][1]
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                while x >= 0 and x < w and y >= 0 and y < h:
                    antinodes.add((x, y))
                    x += dx
                    y += dy

    print(len(antinodes))


part1()
part2()
