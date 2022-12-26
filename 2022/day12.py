#!/usr/bin/env python3

input = open("day12.txt").read().strip()


class HeightMap:
    def __init__(self, input: str) -> None:
        self.locations = {}
        self.marked = set()

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

    def height(self, position):
        h = self.locations[position]
        return ord(h)

    def mark(self, position):
        self.marked.add(position)

    def is_marked(self, position):
        return position in self.marked or position not in self.locations

    def get_locations_at(self, elevation):
        return [l for l, a in self.locations.items() if a == elevation]


class Path:
    def __init__(self, heightmap: HeightMap, init: list) -> None:
        self.heightmap = heightmap
        self.positions = init

    def move(self, direction):
        current = self.positions[-1]

        if direction == "up":
            destination = (current[0] - 1, current[1])
        elif direction == "down":
            destination = (current[0] + 1, current[1])
        elif direction == "left":
            destination = (current[0], current[1] - 1)
        elif direction == "right":
            destination = (current[0], current[1] + 1)

        if not self.heightmap.is_marked(destination):
            if self.heightmap.height(destination) - self.heightmap.height(current) <= 1:
                self.positions.append(destination)
                self.heightmap.mark(destination)
                return destination

    def fork(self):
        newpath = Path(self.heightmap, self.positions.copy())
        return newpath

    def steps(self):
        return len(self.positions) - 1


def find_fewest_steps(start):
    heightmap = HeightMap(input)
    paths = {Path(heightmap, [start])}

    while True:
        if len(paths) == 0:
            return -1

        copy = paths
        paths = set()

        for path in copy:
            for direction in ("up", "down", "left", "right"):
                fork = path.fork()
                position = fork.move(direction)

                if not position:
                    continue

                if position == heightmap.E:
                    return fork.steps()

                paths.add(fork)


def part1():
    heightmap = HeightMap(input)
    return find_fewest_steps(heightmap.S)


def part2():
    heightmap = HeightMap(input)
    starts = heightmap.get_locations_at("a")
    fewests = set()

    for i in range(len(starts)):
        print(f"{i}/{len(starts)}", end="\r")

        start = starts[i]
        steps = find_fewest_steps(start)
        if steps > 0:
            fewests.add(steps)

    return min(fewests)


if __name__ == "__main__":
    print("--- Day 12: Hill Climbing Algorithm ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
