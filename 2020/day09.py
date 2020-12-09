#!/usr/bin/env python3


class Day9:
    def __init__(self, inputs):
        self.numbers = [int(x) for x in inputs.split('\n')]

    def check(self, preamble, number):
        length = len(preamble)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if preamble[i] != preamble[j]:
                    if preamble[i] + preamble[j] == number:
                        return preamble[i], preamble[j]

    def part1(self):
        length = 25
        index = 0
        while index + length < len(self.numbers):
            preamble = self.numbers[index: index + length]
            number = self.numbers[index + length]
            if not self.check(preamble, number):
                self.weakness = number
                return number
            index += 1

    def part2(self):
        length = 2
        while length < len(self.numbers):
            index = 0
            while index + length < len(self.numbers):
                numbers = self.numbers[index: index + length]
                if sum(numbers) == self.weakness:
                    return min(numbers) + max(numbers)
                index += 1
            length += 1


def main():
    inputs = open("day09.txt").read().strip()
    day9 = Day9(inputs)
    print(f'Part 1: {day9.part1()}')
    print(f'Part 2: {day9.part2()}')


if __name__ == "__main__":
    main()
