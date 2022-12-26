#!/usr/bin/env python3

input = open("day12.txt").read().strip()


class HeightMap:
    def __init__(self, input: str) -> None:
        self.locations = {}

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


class Path:
    def __init__(self, heightmap: HeightMap) -> None:
        self.heightmap = heightmap
        self.positions = [self.heightmap.S]

    def check(self, direction):
        curr_position = self.positions[-1]

        if direction == "up":
            dest_position = (curr_position[0] - 1, curr_position[1])
        elif direction == "down":
            dest_position = (curr_position[0] + 1, curr_position[1])
        elif direction == "left":
            dest_position = (curr_position[0], curr_position[1] - 1)
        elif direction == "right":
            dest_position = (curr_position[0], curr_position[1] + 1)

        if dest_position in self.heightmap.locations and dest_position not in self.positions:
            curr_height = self.heightmap.height(curr_position)
            dest_height = self.heightmap.height(dest_position)
            if dest_height - curr_height <= 1:
                return dest_position

    def move(self, positon):
        self.positions.append(positon)

    def fork(self):
        newpath = Path(self.heightmap)
        newpath.positions = self.positions.copy()
        return newpath


def part1():
    heightmap = HeightMap(input.split("\n"))
    paths = {Path(heightmap)}

    step = 0
    while True:
        step += 1
        print(step, end="\r")

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
