#!/usr/bin/env python3

from computer import Intcode

STATIONARY = 0
PULLED = 1

class Day19:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]
        
    def scan(self, point):
        computer = Intcode(self.codes)
        while True:
            status = computer.run()
            if status == Intcode.INPUT:
                computer.input(list(point))
            if status == Intcode.OUTPUT:
                result = computer.output()
            elif status == Intcode.HALT:
                break
        return result

    def is_within(self, closest, area):
        tr = (closest[0] + area[0] - 1, closest[1])
        bl = (closest[0], closest[1] + area[1] - 1)
        for point in [tr, bl]:
            result = self.scan(point)
            if result != PULLED:
                return False
        return True

    def find_next_topright(self, current):
        dx, dy = 1, 1
        while self.scan((current[0] + dx, current[1])) is PULLED:
            dx += 1
        while self.scan((current[0] + dx, current[1] + dy)) is STATIONARY:
            dy += 1
        return (current[0] + dx, current[1] + dy)

    def part1(self):
        affected = 0
        area = (50, 50)
        for y in range(area[1]):
            for x in range(area[0]):
                point = (x, y)
                result = self.scan(point)
                if result == STATIONARY:
                    print('.', end='')
                elif result == PULLED:
                    print('#', end='')
                    affected += 1
            print('')
        return affected

    def part2(self):
        closest = (0, 0)
        area = (100, 100)
        while not self.is_within(closest, area):
            print(closest, end='\r')
            topright = (closest[0] + area[0] - 1, closest[1])
            topright = self.find_next_topright(topright)
            closest = (topright[0] - area[0] + 1, topright[1])
        return closest[0] * 10000 + closest[1]

def main():
    program = open('day19.txt').read().strip()
    day19 = Day19(program)
    print(f'Part 1: {day19.part1()}')
    print(f'Part 2: {day19.part2()}')

if __name__ == "__main__":
    main()
