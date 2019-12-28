#!/usr/bin/env python3

import math

def requirements1(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel

def requirements2(mass):
    total = 0
    fuel = mass
    while True:
        fuel = requirements1(fuel)
        if fuel <= 0:
            break
        total += fuel
    return total

def main():
    with open('day1.txt') as f:
        inputs = f.read().strip()
        masses = [int(x) for x in inputs.split('\n')]

        # Part 1
        sum = 0
        for mass in masses:
            sum += requirements1(mass)
        print("Part1:", sum)

        # Part 2
        sum = 0
        for mass in masses:
            sum += requirements2(mass)
        print("Part2:", sum)

if __name__ == "__main__":
    main()