import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    height = len(lines)
    width = len(lines[0])

    diagram = dict()
    for y in range(height):
        for x in range(width):
            diagram[(x, y)] = lines[y][x]

    return diagram, width, height


DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]


def part1():
    diagram, width, height = input()

    rolls = []
    for x in range(width):
        for y in range(height):
            if diagram[(x, y)] != "@":
                continue

            count = 0
            for dx, dy in DIRECTIONS:
                px, py = x + dx, y + dy
                if 0 <= px < width and 0 <= py < height:
                    if diagram[(px, py)] == "@":
                        count += 1

            if count < 4:
                rolls.append((x, y))

    print("part1: ", len(rolls))


def _access(diagram, width, height):
    rolls = []
    for x in range(width):
        for y in range(height):
            if diagram[(x, y)] != "@":
                continue

            count = 0
            for dx, dy in DIRECTIONS:
                px, py = x + dx, y + dy
                if 0 <= px < width and 0 <= py < height:
                    if diagram[(px, py)] == "@":
                        count += 1

            if count < 4:
                rolls.append((x, y))
    return rolls


def part2():
    diagram, width, height = input()

    total = 0
    while True:
        rolls = _access(diagram, width, height)
        if not rolls:
            break

        for pos in rolls:
            diagram[pos] = "."

        total += len(rolls)

    print("part2: ", total)


part1()
part2()
