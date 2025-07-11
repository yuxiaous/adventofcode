import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    return [[int(h) if h != "." else -1 for h in line] for line in input.split("\n")]


def part1():
    map = input()
    h, w = len(map), len(map[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    trailheads = []
    for y in range(h):
        for x in range(w):
            if map[y][x] == 0:
                trailheads.append((x, y))

    scores = []
    for trailhead in trailheads:
        trails = set({trailhead})
        for height in range(9):
            positions = trails
            trails = set()
            for p in positions:
                for d in directions:
                    x, y = p[0] + d[0], p[1] + d[1]
                    if x in range(w) and y in range(h) and map[y][x] == height + 1:
                        trails.add((x, y))
        scores.append(len(trails))
    print(sum(scores))


def part2():
    map = input()
    h, w = len(map), len(map[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    trailheads = []
    for y in range(h):
        for x in range(w):
            if map[y][x] == 0:
                trailheads.append((x, y))

    ratings = []
    for trailhead in trailheads:
        trails = [[trailhead]]
        for height in range(9):
            last = trails
            trails = []
            for trail in last:
                for d in directions:
                    x = trail[-1][0] + d[0]
                    y = trail[-1][1] + d[1]
                    if x in range(w) and y in range(h) and map[y][x] == height + 1:
                        trails.append(trail + [(x, y)])
        ratings.append(len(trails))
    print(sum(ratings))


part1()
part2()
