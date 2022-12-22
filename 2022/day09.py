#!/usr/bin/env python3
import re

input = open("day09.txt").read().strip()


class Rope:
    def __init__(self, length) -> None:
        self.start = (0, 0)
        self.knots = [list(self.start) for _ in range(length)]

    def move(self, direction):
        # head
        head = self.knots[0]
        if direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1
        elif direction == "L":
            head[0] -= 1
        elif direction == "R":
            head[0] += 1

        # each knot further down
        for i in range(1, len(self.knots)):
            tail = self.knots[i]
            head = self.knots[i - 1]

            if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
                if head[1] > tail[1]:
                    tail[1] += 1
                elif head[1] < tail[1]:
                    tail[1] -= 1
                if head[0] > tail[0]:
                    tail[0] += 1
                elif head[0] < tail[0]:
                    tail[0] -= 1

        return tuple(self.knots[-1])

    def visualize(self, range_x, range_y):
        for y in reversed(range_y):
            for x in range_x:
                while True:
                    position = (x, y)
                    knots = [tuple(x) for x in self.knots]
                    if position in knots:
                        i = knots.index(position)
                        print(i if i > 0 else "H", end="")
                        break

                    if position == self.start:
                        print("s", end="")
                        break

                    print(".", end="")
                    break

            print("")
        print("")


def simulate(rope: Rope):
    visitd = set()

    for motion in input.split("\n"):
        match = re.match(r"([UDLR]) (\d+)", motion)
        if match:
            direction = match.groups()[0]
            step = int(match.groups()[1])

            for _ in range(step):
                tail = rope.move(direction)
                visitd.add(tail)

    return len(visitd)


def part1():
    return simulate(Rope(2))


def part2():
    return simulate(Rope(10))


if __name__ == "__main__":
    print("--- Day 9: Rope Bridge ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
