#!/usr/bin/env python3

from computer import Intcode

class Day2:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def set_noun_verb(self, computer, noun, verb):
        computer.memory[1] = noun
        computer.memory[2] = verb

    def part1(self):
        computer = Intcode(self.codes)
        self.set_noun_verb(computer, 12, 2)
        computer.run()
        return computer.memory[0]

    def part2(self):
        OUTPUT = 19690720
        for noun in range(0, 100):
            for verb in range(0, 100):
                computer = Intcode(self.codes)
                self.set_noun_verb(computer, noun, verb)
                computer.run()
                if computer.memory[0] == OUTPUT:
                    return 100 * noun + verb

def main():
    program = open('day2.txt').read().strip()
    day2 = Day2(program)
    print(f'Part 1: {day2.part1()}')
    print(f'Part 2: {day2.part2()}')

if __name__ == "__main__":
    main()
