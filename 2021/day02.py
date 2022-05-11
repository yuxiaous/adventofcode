#!/usr/bin/env python3

input = open('day02.txt').read().strip().split('\n')


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def forward(self, num):
        self.horizontal += int(num)

    def down(self, num):
        self.depth += int(num)

    def up(self, num):
        self.depth -= int(num)

    def execute(self, instruction):
        command, num = instruction.split()
        if command == 'forward':
            self.forward(num)
        elif command == 'down':
            self.down(num)
        elif command == 'up':
            self.up(num)


def part1(input):
    submarine = Submarine()
    for instruction in input:
        submarine.execute(instruction)
    return submarine.horizontal * submarine.depth


def part2(input):
    pass


print("--- Day 2: Dive! ---")
print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')
