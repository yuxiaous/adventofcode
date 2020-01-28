#!/usr/bin/env python3

from computer import Intcode
import curses

class ArcadeCabinet:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4 

    def __init__(self, codes):
        self.computer = Intcode(codes)
        self.screen_size = (37, 26)
        self.tiles = [ArcadeCabinet.EMPTY] * self.screen_size[0] * self.screen_size[1]
        self.score = 0

        self._pos_ball = 0
        self._pos_paddle = 0

    def play(self, stdscr = None):
        while True:
            status = self.computer.run()
            if status == Intcode.INPUT:
                # auto play
                if self._pos_ball > self._pos_paddle:
                    self.computer.input(1)
                elif self._pos_ball < self._pos_paddle:
                    self.computer.input(-1)
                else:
                    self.computer.input(0)

            elif status == Intcode.OUTPUT:
                values = self.computer.output(3)
                if values:
                    x = values[0]
                    y = values[1]
                    tile_id = values[2]
                    if x >= 0 and y >= 0:
                        self.set_tile_id(x, y, tile_id)
                        # auto play
                        if tile_id == ArcadeCabinet.BALL:
                            self._pos_ball = x
                        if tile_id == ArcadeCabinet.PADDLE:
                            self._pos_paddle = x
                    elif x == -1 and y == 0:
                        self.score = tile_id

                    if stdscr:
                        self.refresh(stdscr)

            elif status == Intcode.HALT:
                break

    def set_tile_id(self, x, y, tile_id):
        w = self.screen_size[0]
        h = self.screen_size[1]
        if x < w and y < h:
            self.tiles[y * w + x] = tile_id

    def get_tile(self, tile_id):
        if tile_id == ArcadeCabinet.EMPTY:
            return ' '
        elif tile_id == ArcadeCabinet.WALL:
            return '■'
        elif tile_id == ArcadeCabinet.BLOCK:
            return '□'
        elif tile_id == ArcadeCabinet.PADDLE:
            return '▬'
        elif tile_id == ArcadeCabinet.BALL:
            return 'o'

    def display(self):
        w = self.screen_size[0]
        h = self.screen_size[1]
        for y in range(h):
            for x in range(w):
                tile_id = self.tiles[y * w + x]
                tile = self.get_tile(tile_id)
                print(tile, end='')
            print('')

    def refresh(self, stdscr):
        stdscr.clear()

        w = self.screen_size[0]
        h = self.screen_size[1]
        for y in range(h):
            for x in range(w):
                tile_id = self.tiles[y * w + x]
                tile = self.get_tile(tile_id)
                stdscr.addch(y, x, tile)
        stdscr.addstr(h, 0, f'Score: {self.score}')

        stdscr.refresh()

class Day13:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def part1(self):
        arcade = ArcadeCabinet(self.codes)
        arcade.play()
        arcade.display()
        return arcade.tiles.count(ArcadeCabinet.BLOCK)

    def part2(self):
        arcade = ArcadeCabinet(self.codes)
        arcade.computer.memory[0] = 2
        # arcade.play()
        curses.wrapper(arcade.play)
        arcade.display()
        return arcade.score

def main():
    program = open('day13.txt').read().strip()
    day13 = Day13(program)
    print(f'Part 1: {day13.part1()}')
    print(f'Part 2: {day13.part2()}')

if __name__ == "__main__":
    main()
