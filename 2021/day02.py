#!/usr/bin/env python3

input = open('day02.txt').read().strip().split('\n')


class Submarine:
    def forward(self, num): pass
    def down(self, num): pass
    def up(self, num): pass

    def execute(self, instruction):
        command, num = instruction.split()
        if command == 'forward':
            self.forward(num)
        elif command == 'down':
            self.down(num)
        elif command == 'up':
            self.up(num)


class Submarine1(Submarine):
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def forward(self, num):
        self.horizontal += int(num)

    def down(self, num):
        self.depth += int(num)

    def up(self, num):
        self.depth -= int(num)


class Submarine2(Submarine):
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def forward(self, num):
        self.horizontal += int(num)
        self.depth += self.aim * int(num)

    def down(self, num):
        self.aim += int(num)

    def up(self, num):
        self.aim -= int(num)


def part1(input):
    submarine = Submarine1()
    for instruction in input:
        submarine.execute(instruction)
    return submarine.horizontal * submarine.depth


def part2(input):
    submarine = Submarine2()
    for instruction in input:
        submarine.execute(instruction)
    return submarine.horizontal * submarine.depth


if __name__ == '__main__':
    print("--- Day 2: Dive! ---")
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
