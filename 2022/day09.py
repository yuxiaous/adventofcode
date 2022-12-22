#!/usr/bin/env python3
import re

input = open("day09.txt").read().strip()


class Rope:
    def __init__(self) -> None:
        self.start = (0, 0)
        self.head = self.start
        self.tail = self.start

    def move(self, direction):
        # head
        if direction == "U":
            self.head = (self.head[0], self.head[1] + 1)
        elif direction == "D":
            self.head = (self.head[0], self.head[1] - 1)
        elif direction == "L":
            self.head = (self.head[0] - 1, self.head[1])
        elif direction == "R":
            self.head = (self.head[0] + 1, self.head[1])

        # tail
        if self.head[0] - self.tail[0] > 1:
            self.tail = (self.head[0] - 1, self.head[1])
        elif self.head[0] - self.tail[0] < -1:
            self.tail = (self.head[0] + 1, self.head[1])
        elif self.head[1] - self.tail[1] > 1:
            self.tail = (self.head[0], self.head[1] - 1)
        elif self.head[1] - self.tail[1] < -1:
            self.tail = (self.head[0], self.head[1] + 1)


def part1():
    visitd = set()

    rope = Rope()
    for motion in input.split("\n"):
        match = re.match(r"([UDLR]) (\d+)", motion)
        if match:
            direction = match.groups()[0]
            step = int(match.groups()[1])

            for _ in range(step):
                rope.move(direction)
                visitd.add(rope.tail)

    return len(visitd)


def part2():
    pass


if __name__ == "__main__":
    print("--- Day 9: Rope Bridge ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
