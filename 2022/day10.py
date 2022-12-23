#!/usr/bin/env python3
import re

input = open("day10.txt").read().strip()


class CPU:
    def __init__(self, program: str) -> None:
        self.instructions = program.split("\n")
        self.X = 1
        self.V = 0

        self.index = 0
        self.cycle = 0
        self.command = None

    def start_cycle(self) -> bool:
        if self.cycle > 0:
            return True

        try:
            instruction = self.instructions[self.index]
            self.index += 1
        except:
            return False

        command = instruction.split(" ")
        self.command = command[0]

        if self.command == "noop":
            self.cycle = 1
            return True

        elif self.command == "addx":
            self.V = int(command[1])
            self.cycle = 2
            return True

        return False

    def during_cycle(self):
        if self.cycle > 0:
            self.cycle -= 1

    def after_cycle(self):
        if self.cycle == 0:
            if self.command == "addx":
                self.X += self.V


def part1():
    sum = 0

    cpu = CPU(input)
    for clock in range(220):
        # start
        if cpu.start_cycle():
            # during
            cpu.during_cycle()

            cycle = clock + 1
            if cycle in (20, 60, 100, 140, 180, 220):
                strength = cycle * cpu.X
                sum += strength

            # after
            cpu.after_cycle()

    return sum


def part2():
    pass


if __name__ == "__main__":
    print("--- Day 10: Cathode-Ray Tube ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
