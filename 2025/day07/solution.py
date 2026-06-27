import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    lines = input.split("\n")

    height = len(lines)
    width = len(lines[0])

    marks: dict[str, list] = {}
    for y in range(height):
        for x in range(width):
            mark = lines[y][x]
            if mark == ".":
                continue
            if mark not in marks:
                marks[mark] = [(x, y)]
            else:
                marks[mark].append((x, y))

    return marks, width, height


def part1():
    marks, width, height = input()
    beams = set(marks["S"])
    count = 0

    while beams:
        downward = set()

        for x, y in beams:
            if y + 1 >= height:
                continue
            if (x, y + 1) in marks["^"]:
                count += 1
                downward.add((x - 1, y + 1))
                downward.add((x + 1, y + 1))
            else:
                downward.add((x, y + 1))

        beams = downward

    print("part1:", count)


part1()
