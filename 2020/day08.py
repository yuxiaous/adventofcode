#!/usr/bin/env python3


class Debugger:
    HALTING = 1
    RUNNING = 2

    def __init__(self, program):
        lines = [line.split(' ') for line in program.split('\n')]
        self.instructions = [(line[0], int(line[1])) for line in lines]
        self.accumulator = 0
        self.address = 0
        self.dispatch = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }

    def acc(self, arg):
        self.accumulator += arg
        self.address += 1

    def jmp(self, arg):
        self.address += arg

    def nop(self, arg):
        self.address += 1

    def execute(self):
        if self.address >= len(self.instructions):
            return self.HALTING

        opt, arg = self.instructions[self.address]
        self.dispatch[opt](arg)
        return self.RUNNING

    def run(self):
        once = set()
        while True:
            if self.address not in once:
                once.add(self.address)
            else:
                return self.address + 1
            if self.execute() == self.HALTING:
                return 0

    def fix_from(self, address):
        while True:
            opt, arg = self.instructions[address]
            if opt == 'jmp':
                self.instructions[address] = ('nop', arg)
                return address + 1
            elif opt == 'nop':
                self.instructions[address] = ('jmp', arg)
                return address + 1
            address += 1


class Day8:
    def __init__(self, inputs):
        self.program = inputs
        pass

    def part1(self):
        debugger = Debugger(self.program)
        debugger.run()
        return debugger.accumulator

    def part2(self):
        address = 0
        while True:
            debugger = Debugger(self.program)
            address = debugger.fix_from(address)
            if debugger.run() == 0:
                return debugger.accumulator


def main():
    inputs = open("day08.txt").read().strip()
    day8 = Day8(inputs)
    print(f'Part 1: {day8.part1()}')
    print(f'Part 2: {day8.part2()}')


if __name__ == "__main__":
    main()
