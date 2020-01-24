#!/usr/bin/env python3

from computer import Intcode
import time

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

    def play(self):
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
                        self._set_tile(x, y, tile_id)
                    elif x == -1 and y == 0:
                        self.score = tile_id
                    self.display()
                    time.sleep(1/60)

            elif status == Intcode.HALT:
                break

    def _set_tile(self, x, y, tile_id):
        w = self.screen_size[0]
        h = self.screen_size[1]
        if x < w and y < h:
            self.tiles[y * w + x] = tile_id

        # auto play
        if tile_id == ArcadeCabinet.BALL:
            self._pos_ball = x
        if tile_id == ArcadeCabinet.PADDLE:
            self._pos_paddle = x

    def display(self):
        w = self.screen_size[0]
        h = self.screen_size[1]
        for y in range(h):
            for x in range(w):
                tile_id = self.tiles[y * w + x]
                if tile_id == ArcadeCabinet.EMPTY:
                    print(' ', end='')
                elif tile_id == ArcadeCabinet.WALL:
                    print('■', end='')
                elif tile_id == ArcadeCabinet.BLOCK:
                    print('□', end='')
                elif tile_id == ArcadeCabinet.PADDLE:
                    print('▬', end='')
                elif tile_id == ArcadeCabinet.BALL:
                    print('o', end='')
            print('')
        print('')

class Day13:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def part1(self):
        arcade = ArcadeCabinet(self.codes)
        arcade.play()

        count = 0
        for tile_id in arcade.tiles:
            if tile_id == ArcadeCabinet.BLOCK:
                count += 1
        return count

    def part2(self):
        arcade = ArcadeCabinet(self.codes)
        arcade.computer.memory[0] = 2
        arcade.play()
        return arcade.score

def main():
    program = open('day13.txt').read().strip()
    day13 = Day13(program)
    print(f'Part 1: {day13.part1()}')
    print(f'Part 2: {day13.part2()}')

if __name__ == "__main__":
    main()
