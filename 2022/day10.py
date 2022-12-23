#!/usr/bin/env python3
import re

input = open("day10.txt").read().strip()


class CPU:
    def __init__(self, program: str) -> None:
        self.instructions = program.split("\n")
        self.X = 1
        self.V = 0
        self.cycle = 0

        self.index = 0
        self.command = None
        self.remaining = 0

    def start_cycle(self) -> bool:
        self.cycle += 1

        if self.remaining > 0:
            return True

        try:
            instruction = self.instructions[self.index]
            self.index += 1
        except:
            return False

        command = instruction.split(" ")
        self.command = command[0]

        if self.command == "noop":
            self.remaining = 1
            return True

        elif self.command == "addx":
            self.V = int(command[1])
            self.remaining = 2
            return True

        return False

    def during_cycle(self):
        if self.remaining > 0:
            self.remaining -= 1

    def end_cycle(self):
        if self.remaining == 0:
            if self.command == "addx":
                self.X += self.V


class CRT:
    def __init__(self) -> None:
        self.cycle = 0
        self.wide = 40
        self.high = 6
        self.pixels = {}

        for r in range(self.high):
            for c in range(self.wide):
                self.pixels[(r, c)] = "."

    def during_cycle(self, sprite):
        self.cycle += 1

        position = self.cycle - 1
        position %= self.wide * self.high

        r = int(position / self.wide)
        c = int(position % self.wide)

        self.pixels[(r, c)] = "#" if c in sprite else "."

    def draw(self):
        output = []
        for r in range(self.high):
            for c in range(self.wide):
                pixel = self.pixels[(r, c)]
                output.append(pixel)
            output.append("\n")
        return "".join(output)


def part1():
    sum = 0

    cpu = CPU(input)
    while cpu.start_cycle():
        cpu.during_cycle()

        if cpu.cycle in (20, 60, 100, 140, 180, 220):
            strength = cpu.cycle * cpu.X
            sum += strength

        cpu.end_cycle()

    return sum


def part2():
    crt = CRT()
    cpu = CPU(input)
    while cpu.start_cycle():
        cpu.during_cycle()

        sprite = [cpu.X - 1, cpu.X, cpu.X + 1]
        crt.during_cycle(sprite)

        cpu.end_cycle()

    return crt.draw()


if __name__ == "__main__":
    print("--- Day 10: Cathode-Ray Tube ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: \n{part2()}")
