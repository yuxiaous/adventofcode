import os
from enum import Enum

os.chdir(os.path.dirname(__file__))


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class Map:
    pass


class Guard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def forward(self):
        if self.direction == Direction.Up:
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == Direction.Right:
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == Direction.Down:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == Direction.Left:
            self.position = (self.position[0] - 1, self.position[1])

    def turn(self):
        if self.direction == Direction.Up:
            self.direction = Direction.Right
        elif self.direction == Direction.Right:
            self.direction = Direction.Down
        elif self.direction == Direction.Down:
            self.direction = Direction.Left
        elif self.direction == Direction.Left:
            self.direction = Direction.Up

    def check(self, map):
        h = len(map)
        w = len(map[0])

        if self.direction == Direction.Up:
            if self.position[1] - 1 >= 0:
                return map[self.position[1] - 1][self.position[0]]
        elif self.direction == Direction.Right:
            if self.position[0] + 1 < w:
                return map[self.position[1]][self.position[0] + 1]
        elif self.direction == Direction.Down:
            if self.position[1] + 1 < h:
                return map[self.position[1] + 1][self.position[0]]
        elif self.direction == Direction.Left:
            if self.position[0] - 1 >= 0:
                return map[self.position[1]][self.position[0] - 1]
        return None


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

    visited = set()
    guard = Guard(search(map, "^"), Direction.Up)
    while True:
        visited.add(guard.position)

        front = guard.check(map)
        if front == None:
            break
        elif front == "#":
            guard.turn()
        else:
            guard.forward()

    print(len(visited))


part1()
