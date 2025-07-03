import os

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").readlines()
    return [[x for x in line.strip()] for line in lines]


def part1():
    word = "XMAS"
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    count = 0
    letters = input()
    for y in range(len(letters)):
        for x in range(len(letters[0])):
            for dx, dy in direction:
                if dx > 0 and x > len(letters[0]) - len(word):
                    continue
                elif dx < 0 and x < len(word) - 1:
                    continue
                if dy > 0 and y > len(letters) - len(word):
                    continue
                elif dy < 0 and y < len(word) - 1:
                    continue

                for i in range(len(word)):
                    if letters[y + dy * i][x + dx * i] != word[i]:
                        break
                else:
                    count += 1
    print(count)


def part2():
    xmax = [
        {(0, 0): "A", (-1, -1): "M", (-1, 1): "M", (1, 1): "S", (1, -1): "S"},
        {(0, 0): "A", (-1, 1): "M", (1, 1): "M", (1, -1): "S", (-1, -1): "S"},
        {(0, 0): "A", (1, 1): "M", (1, -1): "M", (-1, -1): "S", (-1, 1): "S"},
        {(0, 0): "A", (1, -1): "M", (-1, -1): "M", (-1, 1): "S", (1, 1): "S"},
    ]

    count = 0
    letters = input()
    for y in range(len(letters)):
        for x in range(len(letters[0])):
            if x <= 0 or x >= len(letters[0]) - 1:
                continue
            if y <= 0 or y >= len(letters) - 1:
                continue

            for mas in xmax:
                for (dx, dy), c in mas.items():
                    if letters[y + dy][x + dx] != c:
                        break
                else:
                    count += 1
    print(count)


part1()
part2()
