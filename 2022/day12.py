#!/usr/bin/env python3

input = open("day12.txt").read().strip()


class HeightMap:
    def __init__(self, input: str) -> None:
        self.locations = {}

        input = input.split("\n")
        for r in range(len(input)):
            for c in range(len(input[r])):
                self.locations[(r, c)] = input[r][c]

        for p, h in self.locations.items():
            if h == "S":
                self.S = p
                self.locations[p] = "a"
            elif h == "E":
                self.E = p
                self.locations[p] = "z"

        self.unmarks = self.locations.copy()

    def height(self, position):
        h = self.locations[position]
        return ord(h)

    def mark(self, position):
        self.unmarks.pop(position)


class Path:
    def __init__(self, heightmap: HeightMap) -> None:
        self.heightmap = heightmap
        self.positions = [self.heightmap.S]

    def check(self, direction):
        current = self.positions[-1]

        if direction == "up":
            destination = (current[0] - 1, current[1])
        elif direction == "down":
            destination = (current[0] + 1, current[1])
        elif direction == "left":
            destination = (current[0], current[1] - 1)
        elif direction == "right":
            destination = (current[0], current[1] + 1)

        if destination in self.heightmap.unmarks:
            if self.heightmap.height(destination) - self.heightmap.height(current) <= 1:
                return destination

    def move(self, positon):
        self.positions.append(positon)
        self.heightmap.mark(positon)

    def fork(self):
        newpath = Path(self.heightmap)
        newpath.positions = self.positions.copy()
        return newpath


def part1():
    heightmap = HeightMap(input)
    paths = {Path(heightmap)}

    step = 0
    while True:
        step += 1

        copy = paths
        paths: set[Path] = set()

        for path in copy:
            for direction in ("up", "down", "left", "right"):
                position = path.check(direction)
                if not position:
                    continue

                if position == heightmap.E:
                    return step

                fork = path.fork()
                fork.move(position)

                if all(position not in p.positions for p in paths):
                    paths.add(fork)


def part2():
    pass


if __name__ == "__main__":
    print("--- Day 12: Hill Climbing Algorithm ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
