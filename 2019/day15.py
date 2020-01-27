#!/usr/bin/env python3

from computer import Intcode
import curses

class RepairDroid:
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    UNEXPLORED = -1
    WALL = 0
    OPEN = 1
    OXYGEN = 2

    def __init__(self, codes):
        self.computer = Intcode(codes)

    def explore(self, stdscr = None):
        area = {}
        area['width'] = 46
        area['height'] = 46
        area['start'] = (int(area['width'] / 2), int(area['height'] / 2))
        area['oxygen'] = None
        area['map'] = [RepairDroid.UNEXPLORED] * area['width'] * area['height']

        direction = RepairDroid.NORTH
        curr_pos = area['start']
        next_pos = (curr_pos[0], curr_pos[1] - 1)

        def p2i(pos):
            return pos[1] * area['height'] + pos[0]
        def turn_left():
            nonlocal direction
            if direction == RepairDroid.NORTH:
                direction = RepairDroid.WEST
            elif direction == RepairDroid.WEST:
                direction = RepairDroid.SOUTH
            elif direction == RepairDroid.SOUTH:
                direction = RepairDroid.EAST
            elif direction == RepairDroid.EAST:
                direction = RepairDroid.NORTH
        def turn_right():
            nonlocal direction
            if direction == RepairDroid.NORTH:
                direction = RepairDroid.EAST
            elif direction == RepairDroid.EAST:
                direction = RepairDroid.SOUTH
            elif direction == RepairDroid.SOUTH:
                direction = RepairDroid.WEST
            elif direction == RepairDroid.WEST:
                direction = RepairDroid.NORTH

        while True:
            status = self.computer.run()

            if status == Intcode.INPUT:
                if direction == RepairDroid.NORTH:
                    next_pos = (curr_pos[0], curr_pos[1] - 1)
                elif direction == RepairDroid.SOUTH:
                    next_pos = (curr_pos[0], curr_pos[1] + 1)
                elif direction == RepairDroid.WEST:
                    next_pos = (curr_pos[0] - 1, curr_pos[1])
                elif direction == RepairDroid.EAST:
                    next_pos = (curr_pos[0] + 1, curr_pos[1])
                self.computer.input(direction)

            elif status == Intcode.OUTPUT:
                status = self.computer.output()
                area['map'][p2i(next_pos)] = status
                if status == RepairDroid.WALL:
                    turn_left()
                elif status == RepairDroid.OPEN:
                    curr_pos = next_pos
                    turn_right()
                elif status == RepairDroid.OXYGEN:
                    area['oxygen'] = next_pos
                    curr_pos = next_pos
                    turn_right()

                if stdscr:
                    self.draw(area, curr_pos, stdscr)

                if next_pos == area['start']:
                    break

            elif status == Intcode.HALT:
                break

        return area

    def draw(self, area, current = None, stdscr = None):
        amap = area['map']
        width = area['width']
        height = area['height']
        start = area['start']
        oxygen = area['oxygen']
        current = current or start

        if stdscr:
            stdscr.clear()

        for y in range(height):
            for x in range(width):
                position = (x, y)
                location = amap[y * height + x]
                if position == current:
                    tile = 'D'
                elif position == start:
                    tile = 'X'
                elif position == oxygen:
                    tile = 'O'
                elif location == RepairDroid.UNEXPLORED:
                    tile = ' '
                elif location == RepairDroid.WALL:
                    tile = '#'
                elif location == RepairDroid.OPEN:
                    tile = '.'
                elif location == RepairDroid.OXYGEN:
                    tile = 'O'
                if stdscr:
                    stdscr.addch(y, x, tile)
                else:
                    print(tile, end='')
            if not stdscr:
                print('')

        if stdscr:
            stdscr.refresh()
            
class Day15:
    def __init__(self, program):
        codes = [int(x) for x in program.split(',')]
        droid = RepairDroid(codes)
        self.area = curses.wrapper(droid.explore)
        # area = droid.explore()
        droid.draw(self.area)

    def part1(self):
        pass

    def part2(self):
        pass

def main():
    program = open('day15.txt').read().strip()
    day15 = Day15(program)
    print(f'Part 1: {day15.part1()}')
    print(f'Part 2: {day15.part2()}')

if __name__ == "__main__":
    main()
