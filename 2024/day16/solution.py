import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    return [[t for t in l] for l in input.split("\n")]


def find_tile(map, tile):
    h, w = len(map), len(map[0])
    for y in range(h):
        for x in range(w):
            if map[y][x] == tile:
                return (x, y)


def part1():
    map = input()
    start = find_tile(map, "S")
    end = find_tile(map, "E")

    scores = set()
    records = {}
    tracks = set({(0, start, (1, 0))})

    while len(tracks) > 0:
        score, (x, y), (dx, dy) = tracks.pop()

        record = records.get((x, y, dx, dy), -1)
        if record >= 0 and score > record:
            continue
        records[(x, y, dx, dy)] = score

        if (x, y) == end:
            scores.add(score)
            continue

        # move forward
        if map[y + dy][x + dx] != "#":
            tracks.add((score + 1, (x + dx, y + dy), (dx, dy)))
        # turn left
        if map[y + dx][x - dy] != "#":
            tracks.add((score + 1000, (x, y), (-dy, dx)))
        # turn right
        if map[y - dx][x + dy] != "#":
            tracks.add((score + 1000, (x, y), (dy, -dx)))

    return min(scores)


print(part1())


def part2():
    map = input()
    start = find_tile(map, "S")
    end = find_tile(map, "E")
    lowest = part1()

    scores = []
    records = {}
    tracks = {(0, start, (1, 0)): set()}

    while len(tracks) > 0:
        (score, (x, y), (dx, dy)), path = tracks.popitem()

        if score > lowest:
            continue

        record = records.get((x, y, dx, dy), -1)
        if record >= 0 and score > record:
            continue

        records[(x, y, dx, dy)] = score
        path.add((x, y))

        if (x, y) == end:
            scores.append((score, path))
            continue

        # move forward
        if map[y + dy][x + dx] != "#":
            tracks[(score + 1, (x + dx, y + dy), (dx, dy))] = path.copy()
        # turn left
        if map[y + dx][x - dy] != "#":
            tracks[(score + 1000, (x, y), (-dy, dx))] = path.copy()
        # turn right
        if map[y - dx][x + dy] != "#":
            tracks[(score + 1000, (x, y), (dy, -dx))] = path.copy()

    tiles = set()
    for score, path in scores:
        for tile in path:
            tiles.add(tile)
    print(len(tiles))


part2()
