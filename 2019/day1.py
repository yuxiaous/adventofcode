#!/usr/bin/env python3

import math

class Day1:
    def __init__(self, inputs):
        self.masses = [int(x) for x in inputs.split('\n')]

    def requirements1(self, mass):
        fuel = math.floor(mass / 3) - 2
        return fuel

    def requirements2(self, mass):
        total = 0
        fuel = mass
        while True:
            fuel = self.requirements1(fuel)
            if fuel <= 0:
                break
            total += fuel
        return total

    def part1(self):
        sum = 0
        for mass in self.masses:
            sum += self.requirements1(mass)
        return sum

    def part2(self):
        sum = 0
        for mass in self.masses:
            sum += self.requirements2(mass)
        return sum

def main():
    inputs = open('day1.txt').read().strip()
    day1 = Day1(inputs)
    print(f'Part 1: {day1.part1()}')
    print(f'Part 2: {day1.part2()}')

if __name__ == "__main__":
    main()
