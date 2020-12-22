#!/usr/bin/env python3

import re

TOP = 0
LEFT = 1
RIGHT = 2
BOTTOM = 3


class Tile:
    def __init__(self, data):
        m = re.match(r'Tile (\d+):\n([\.#\n]+)', data)
        # id
        self.id = int(m.group(1))
        # data
        lines = m.group(2).split('\n')
        self.width = len(lines)
        self.height = len(lines[0])
        self.data = ''.join(lines)
        # lineups
        self.lineups = {}

    def grid(self, row, col):
        return self.data[self.width * row + col]

    def border(self, side):
        if side == TOP:
            return ''.join(self.grid(0, c) for c in range(self.width))
        if side == LEFT:
            return ''.join(self.grid(r, 0) for r in range(self.height))
        if side == RIGHT:
            return ''.join(self.grid(r, self.width-1) for r in range(self.height))
        if side == BOTTOM:
            return ''.join(self.grid(self.height-1, c) for c in range(self.width))


class Day20:
    def __init__(self, inputs):
        # tiles
        self.tiles = {}
        for data in inputs.split('\n\n'):
            tile = Tile(data)
            self.tiles[tile.id] = tile
        # init line up
        self.init_lineups()

    def init_lineups(self):
        def lineup(tile1, tile2):
            sides = {TOP, LEFT, RIGHT, BOTTOM}
            sides1 = set(side for side in sides if not tile1.lineups.get(side))
            sides2 = set(side for side in sides if not tile2.lineups.get(side))
            if len(sides1) == 0 or len(sides2) == 0:
                return
            for side1 in sides1:
                border1 = tile1.border(side1)
                for side2 in sides2:
                    border2 = tile2.border(side2)
                    if border1 == border2 or border1 == border2[::-1]:
                        tile1.lineups[side1] = tile2.id
                        tile2.lineups[side2] = tile2.id
        for tile1 in self.tiles.values():
            for tile2 in self.tiles.values():
                if tile1.id != tile2.id:
                    lineup(tile1, tile2)

    def part1(self):
        result = 1
        for tile in self.tiles.values():
            if len(tile.lineups) == 2:
                result *= tile.id
        return result

    def part2(self):
        pass


def main():
    inputs = open("day20.txt").read().strip()
    day20 = Day20(inputs)
    print(f'Part 1: {day20.part1()}')
    print(f'Part 2: {day20.part2()}')


if __name__ == "__main__":
    main()
