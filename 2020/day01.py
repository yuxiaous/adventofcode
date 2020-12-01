#!/usr/bin/env python3

class Day1:
    def __init__(self, inputs):
        self.reports = [int(x) for x in inputs.split('\n')]

    def part1(self):
        length = len(self.reports)
        for i in range(length - 1):
            a = self.reports[i]
            for j in range(i + 1, length):
                b = self.reports[j]

                if a + b == 2020:
                    return a * b, a, b

    def part2(self):
        length = len(self.reports)
        for i in range(length - 2):
            a = self.reports[i]
            for j in range(i + 1, length - 1):
                b = self.reports[j]
                for k in range(j + 1, length):
                    c = self.reports[k]

                    if a + b + c == 2020:
                        return a * b * c, a, b, c

def main():
    inputs = open('day01.txt').read().strip()
    day1 = Day1(inputs)
    print(f'Part 1: {day1.part1()}')
    print(f'Part 2: {day1.part2()}')

if __name__ == "__main__":
    main()
