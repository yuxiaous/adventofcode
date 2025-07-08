import os
from enum import Enum

os.chdir(os.path.dirname(__file__))


class Direction(Enum):
    Up = (0, -1)
    Right = (1, 0)
    Down = (0, 1)
    Left = (-1, 0)


class Guard:
    def __init__(self, position, direction: Direction):
        self.position = position
        self.direction = direction

    def front(self):
        return (
            self.position[0] + self.direction.value[0],
            self.position[1] + self.direction.value[1],
        )

    def forward(self):
        self.position = self.front()

    def turn(self):
        self.direction = Direction(-self.direction.value[1], self.direction.value[0])

    def check(self, map):
        w, h = len(map[0]), len(map)
        x, y = self.front()

        if x >= 0 and x < w and y >= 0 and y < h:
            return map[y][x]
        return None

    def patrol(self, map):
        steps = set()

        while True:
            steps.add((self.position, self.direction))

            front = self.check(map)
            if front == None:
                return False, steps
            elif front == "#":
                self.turn()
            else:
                self.forward()
            if (self.position, self.direction) in steps:
                return True, steps


def input():
    map = [[p for p in line] for line in open("input.txt").read().strip().split("\n")]
    return map


def search(map, guard):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == guard:
                return (x, y)


def part1():
    map = input()

    guard = Guard(search(map, "^"), Direction.Up)
    _, steps = guard.patrol(map)
    visited = set(s[0] for s in steps)
    print(len(visited))


def part2():
    obstructions = set()

    map = input()
    origin = search(map, "^")
    guard = Guard(origin, Direction.Up)
    _, steps = guard.patrol(map)
    total = len(steps)

    count = 0
    guard = Guard(origin, Direction.Up)
    while True:
        count += 1
        print(f"{count}/{total}", end="\r")

        front = guard.check(map)
        if front == None:
            break
        elif front == "#":
            guard.turn()
        else:
            x, y = guard.front()
            save = map[y][x]
            map[y][x] = "#"

            shadow = Guard(origin, Direction.Up)
            loop, _ = shadow.patrol(map)
            if loop:
                obstructions.add((x, y))

            map[y][x] = save

            guard.forward()

    print("                            ", end="\r")
    print(len(obstructions))


part1()
part2()
