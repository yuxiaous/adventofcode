#!/usr/bin/env python3

from computer import Intcode

# test1 = '1002,4,3,4,33'
# test2 = '1101,100,-1,4,0'
# test3 = '3,9,8,9,10,9,4,9,99,-1,8'
# test4 = '3,9,7,9,10,9,4,9,99,-1,8'
# test5 = '3,3,1108,-1,8,3,4,3,99'
# test6 = '3,3,1107,-1,8,3,4,3,99'
# test7 = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
# test8 = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
# test9 = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'

class Day5:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def test(self, input):
        computer = Intcode(self.codes)
        output = None
        while True:
            res = computer.run()
            if res == Intcode.INPUT:
                computer.input(input)
            elif res == Intcode.OUTPUT:
                output = computer.output()
            elif res == Intcode.HALT:
                break
        return output

    def part1(self):
        return self.test(1)

    def part2(self):
        return self.test(5)

def main():
    program = open('day5.txt').read().strip()
    day5 = Day5(program)
    print(f'Part 1: {day5.part1()}')
    print(f'Part 2: {day5.part2()}')

if __name__ == "__main__":
    main()
