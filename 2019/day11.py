#!/usr/bin/env python3

import io
from computer import Intcode

BLACK = 0
WHITE = 1

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def poskey(pos):
    return pos[0] * 1000 + pos[1]

class PaintingRobot:

    def __init__(self, codes, panels):
        self.brain = Intcode(codes)
        self.direction = UP
        self.position = (0, 0)
        self.panels = panels

    def run(self):
        while True:
            status = self.brain.run()
            if status == Intcode.INPUT:
                color = self.camera()
                self.brain.input(color)

            elif status == Intcode.OUTPUT:
                values = self.brain.output(2)
                if values:
                    self.paint(values[0])
                    self.turn(values[1])

            elif status == Intcode.HALT:
                break

    def camera(self):
        key = poskey(self.position)
        if key in self.panels:
            return self.panels[key]
        else:
            return BLACK
    
    def paint(self, color):
        key = poskey(self.position)
        self.panels[key] = color

    def turn(self, turn):
        if turn == LEFT:
            if self.direction == UP:
                self.direction = LEFT
            elif self.direction == LEFT:
                self.direction = DOWN
            elif self.direction == DOWN:
                self.direction = RIGHT
            elif self.direction == RIGHT:
                self.direction = UP
        elif turn == RIGHT:
            if self.direction == UP:
                self.direction = RIGHT
            elif self.direction == RIGHT:
                self.direction = DOWN
            elif self.direction == DOWN:
                self.direction = LEFT
            elif self.direction == LEFT:
                self.direction = UP

        if self.direction == UP:
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == DOWN:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == LEFT:
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == RIGHT:
            self.position = (self.position[0] + 1, self.position[1])

class Day11:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def part1(self):
        panels = {}
        robot = PaintingRobot(self.codes, panels)
        robot.run()
        return len(panels)

    def part2(self):
        panels = { 0: WHITE }
        robot = PaintingRobot(self.codes, panels)
        robot.run()
        return self.show(panels)

    def show(self, panels):
        points = list(panels.keys())

        width = int(max(points, key=lambda p: int(p / 1000)) / 1000) + 1
        height = int(max(points, key=lambda p: int(p % 1000)) % 1000) + 1

        with io.StringIO() as stream:
            for y in range(height):
                stream.write('\n')
                for x in range(width):
                    key = poskey((x, y))
                    if key in panels and panels[key] == WHITE:
                        stream.write('■')
                    else:
                        stream.write(' ')

            return stream.getvalue()

def main():
    program = open('day11.txt').read().strip()
    day11 = Day11(program)
    print(f'Part 1: {day11.part1()}')
    print(f'Part 2: {day11.part2()}')

if __name__ == "__main__":
    main()
