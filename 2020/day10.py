#!/usr/bin/env python3


class Day10:
    def __init__(self, inputs):
        self.jolts = [int(x) for x in inputs.split('\n')]
        self.jolts.append(0)
        self.jolts.append(max(self.jolts) + 3)
        self.jolts.sort()

    def part1(self):
        count = [0, 0, 0]
        for i in range(len(self.jolts) - 1):
            difference = self.jolts[i+1] - self.jolts[i]
            count[difference-1] += 1
        return count[0] * count[2]

    def part2(self):
        index = 1
        steps = {0: 1}
        while index < len(self.jolts):
            count = 0
            offset = 1
            while True:
                check = index - offset
                if check < 0 or self.jolts[index] - self.jolts[check] > 3:
                    break
                count += steps[check]
                offset += 1
            steps[index] = count
            index += 1
        return count


def main():
    inputs = open("day10.txt").read().strip()
    day10 = Day10(inputs)
    print(f'Part 1: {day10.part1()}')
    print(f'Part 2: {day10.part2()}')


if __name__ == "__main__":
    main()
