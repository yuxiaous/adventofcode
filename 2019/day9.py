#!/usr/bin/env python3

from computer import Intcode

# test1 = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
# test2 = '1102,34915192,34915192,7,4,7,99,0'
# test3 = '104,1125899906842624,99'

class Day9:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def run_program(self, mode):
        keycode = None
        computer = Intcode(self.codes)
        while True:
            status = computer.run()
            if status == Intcode.INPUT:
                computer.input(mode)
            elif status == Intcode.OUTPUT:
                keycode = computer.output()
            elif status == Intcode.HALT:
                break
        return keycode

    def part1(self):
        return self.run_program(1)

    def part2(self):
        return self.run_program(2)

def main():
    program = open('day9.txt').read().strip()
    day9 = Day9(program)
    print(f'Part 1: {day9.part1()}')
    print(f'Part 2: {day9.part2()}')

if __name__ == "__main__":
    main()
