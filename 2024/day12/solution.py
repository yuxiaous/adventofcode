import os
from typing import Dict

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    return [[x for x in line] for line in input.split("\n")]


def part1():
    plots = input()
    h, w = len(plots), len(plots[0])

    plants: Dict[str, list] = {}
    for y in range(h):
        for x in range(w):
            plant = plots[y][x]
            if plant not in plants:
                plants[plant] = []
            plants[plant].append((x, y))

    regions: Dict[str, list] = {}
    for plant in plants:
        regions[plant] = []

        plots = plants[plant]
        while len(plots) > 0:
            region = [plots.pop()]

            def link(x, y):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (x + dx, y + dy) in plots:
                        plots.remove((x + dx, y + dy))
                        region.append((x + dx, y + dy))
                        link(x + dx, y + dy)

            link(region[0][0], region[0][1])

            regions[plant].append(region)

    price = 0
    for plant in plants:
        for region in regions[plant]:
            area = 0
            perimeter = 0
            plots = []

            for x, y in region:
                plots.append((x, y))
                area += 1

                adjacement = 0
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (x + dx, y + dy) in plots:
                        adjacement += 1
                perimeter += 4 - adjacement - adjacement

            price += area * perimeter
    print(price)


part1()


def part2():
    plots = input()
    h, w = len(plots), len(plots[0])

    plants: Dict[str, list] = {}
    for y in range(h):
        for x in range(w):
            plant = plots[y][x]
            if plant not in plants:
                plants[plant] = []
            plants[plant].append((x, y))

    regions: Dict[str, list] = {}
    for plant in plants:
        regions[plant] = []

        plots = plants[plant]
        while len(plots) > 0:
            region = [plots.pop()]

            def link(x, y):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (x + dx, y + dy) in plots:
                        plots.remove((x + dx, y + dy))
                        region.append((x + dx, y + dy))
                        link(x + dx, y + dy)

            link(region[0][0], region[0][1])

            regions[plant].append(region)

    price = 0
    for plant in plants:
        for region in regions[plant]:
            area = 0
            sides = set()

            for x, y in region:
                area += 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (x + dx, y + dy) not in region:
                        xx, yy = x, y
                        while (xx + dy, yy + dx) in region and (
                            xx + dy + dx,
                            yy + dx + dy,
                        ) not in region:
                            xx, yy = xx + dy, yy + dx
                        sides.add((xx, yy, dx, dy))

            price += area * len(sides)

    print(price)


part2()
