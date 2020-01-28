#!/usr/bin/env python3

from computer import Intcode
import curses

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

UNEXPLORED = -1
WALL = 0
OPEN = 1
OXYGEN = 2

class AreaMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start = (int(width / 2), int(height / 2))
        self.oxygen = None
        self.locations = [UNEXPLORED] * width * height

    def set_location(self, pos, location):
        x, y = pos
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            self.locations[y * self.width + x] = location

    def get_location(self, pos):
        x, y = pos
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.locations[y * self.width + x]
        return UNEXPLORED

    def draw(self, current = None, stdscr = None):
        if stdscr:
            stdscr.clear()

        for y in range(self.height):
            for x in range(self.width):
                position = (x, y)
                location = self.get_location(position)
                if position == current:
                    tile = 'D'
                elif position == self.start:
                    tile = 'X'
                elif position == self.oxygen:
                    tile = 'O'
                elif location == WALL:
                    tile = '#'
                elif location == OPEN:
                    tile = '.'
                elif location == OXYGEN:
                    tile = 'O'
                else:
                    tile = ' '
                if stdscr:
                    stdscr.addch(y, x, tile)
                else:
                    print(tile, end='')
            if not stdscr:
                print('')

        if stdscr:
            stdscr.refresh()

    def spread(self, start):
        opened = [start]
        passed = []
        steps = []
        while True:
            steps.append(opened)
            temp = opened

            opened = []
            for pos in temp:
                passed.append(pos)

                north = (pos[0], pos[1] - 1)
                south = (pos[0], pos[1] + 1)
                west = (pos[0] - 1, pos[1])
                east = (pos[0] + 1, pos[1])
                for direction in (north, south, west, east):
                    if direction in passed:
                        continue
                    if self.get_location(direction) in (OPEN, OXYGEN):
                        opened.append(direction)

            if not opened:
                return steps

class RepairDroid:
    def __init__(self, codes):
        self.computer = Intcode(codes)
        self.area = AreaMap(42, 42)
        self.curr_pos = self.area.start
        self.next_pos = None
        self.direction = NORTH

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH
    
    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH

    def _update_next_position(self):
        if self.direction == NORTH:
            self.next_pos = (self.curr_pos[0], self.curr_pos[1] - 1)
        elif self.direction == SOUTH:
            self.next_pos = (self.curr_pos[0], self.curr_pos[1] + 1)
        elif self.direction == WEST:
            self.next_pos = (self.curr_pos[0] - 1, self.curr_pos[1])
        elif self.direction == EAST:
            self.next_pos = (self.curr_pos[0] + 1, self.curr_pos[1])

    def explore(self, stdscr = None):
        if self.area.oxygen:
            return

        while True:
            status = self.computer.run()

            if status == Intcode.INPUT:
                self._update_next_position()
                self.computer.input(self.direction)

            elif status == Intcode.OUTPUT:
                status = self.computer.output()
                self.area.set_location(self.next_pos, status)

                if status == WALL:
                    self.turn_left()
                elif status == OPEN:
                    self.curr_pos = self.next_pos
                    self.turn_right()
                elif status == OXYGEN:
                    self.area.oxygen = self.next_pos
                    self.curr_pos = self.next_pos
                    self.turn_right()

                if stdscr:
                    self.area.draw(self.curr_pos, stdscr)

                if self.next_pos == self.area.start:
                    break

            elif status == Intcode.HALT:
                break
            
class Day15:
    def __init__(self, program):
        codes = [int(x) for x in program.split(',')]
        droid = RepairDroid(codes)
        # droid.explore()
        curses.wrapper(droid.explore)

        self.area = droid.area
        self.area.draw()

    def part1(self):
        steps = self.area.spread(self.area.start)
        for step in steps:
            if self.area.oxygen in step:
                return steps.index(step)

    def part2(self):
        steps = self.area.spread(self.area.oxygen)
        return len(steps) - 1

def main():
    program = open('day15.txt').read().strip()
    day15 = Day15(program)
    print(f'Part 1: {day15.part1()}')
    print(f'Part 2: {day15.part2()}')

if __name__ == "__main__":
    main()
