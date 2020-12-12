#!/usr/bin/env python3

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'


class Ship1:
    def __init__(self):
        self.face = EAST
        self.position = [0, 0]

    def handle(self, instruction):
        action = instruction[0]
        value = instruction[1]
        if action == FORWARD:
            action = self.face
        if action == NORTH:
            self.position[1] += value
        elif action == SOUTH:
            self.position[1] -= value
        elif action == EAST:
            self.position[0] += value
        elif action == WEST:
            self.position[0] -= value
        elif action == LEFT:
            self.turn_left(value)
        elif action == RIGHT:
            self.turn_right(value)

    def turn_left(self, value):
        def turn():
            if self.face == EAST:
                self.face = NORTH
            elif self.face == NORTH:
                self.face = WEST
            elif self.face == WEST:
                self.face = SOUTH
            elif self.face == SOUTH:
                self.face = EAST
        while value:
            value -= 90
            turn()

    def turn_right(self, value):
        def turn():
            if self.face == EAST:
                self.face = SOUTH
            elif self.face == SOUTH:
                self.face = WEST
            elif self.face == WEST:
                self.face = NORTH
            elif self.face == NORTH:
                self.face = EAST
        while value:
            value -= 90
            turn()

    def manhattan(self):
        return abs(self.position[0]) + abs(self.position[1])


class Ship2:
    def __init__(self):
        self.waypoint = [10, 1]
        self.position = [0, 0]

    def handle(self, instruction):
        action = instruction[0]
        value = instruction[1]
        if action == NORTH:
            self.waypoint[1] += value
        elif action == SOUTH:
            self.waypoint[1] -= value
        elif action == EAST:
            self.waypoint[0] += value
        elif action == WEST:
            self.waypoint[0] -= value
        elif action == LEFT:
            while value:
                value -= 90
                self.waypoint = [-self.waypoint[1], self.waypoint[0]]
        elif action == RIGHT:
            while value:
                value -= 90
                self.waypoint = [self.waypoint[1], -self.waypoint[0]]
        elif action == FORWARD:
            offset = [x * value for x in self.waypoint]
            self.position = [sum(x) for x in zip(self.position, offset)]

    def manhattan(self):
        return abs(self.position[0]) + abs(self.position[1])


class Day12:
    def __init__(self, inputs):
        self.instructions = [(x[0], int(x[1:])) for x in inputs.split('\n')]

    def part1(self):
        ship = Ship1()
        for instruction in self.instructions:
            ship.handle(instruction)
        return ship.manhattan()

    def part2(self):
        ship = Ship2()
        for instruction in self.instructions:
            ship.handle(instruction)
        return ship.manhattan()


def main():
    inputs = open("day12.txt").read().strip()
    day12 = Day12(inputs)
    print(f'Part 1: {day12.part1()}')
    print(f'Part 2: {day12.part2()}')


if __name__ == "__main__":
    main()
