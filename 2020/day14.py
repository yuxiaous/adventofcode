#!/usr/bin/env python3

import re


class Day14:
    def __init__(self, inputs):
        self.lines = inputs.split('\n')

    def do_mask1(self, value, mask):
        result = []
        for i in range(len(value)):
            if mask[i] == 'X':
                result.append(value[i])
            else:
                result.append(mask[i])
        return ''.join(result)

    def do_mask2(self, value, mask):
        result = []
        for i in range(len(value)):
            if mask[i] == '0':
                result.append(value[i])
            else:
                result.append(mask[i])
        return ''.join(result)

    def make_mask1(self, x, n):
        mask = ['X'] * 36
        num = '{0:036b}'.format(n)
        for i in range(len(x)):
            mask[-x[i]-1] = num[-i-1]
        return ''.join(mask)

    def part1(self):
        memory = {}
        for line in self.lines:
            match = re.match(r'^mask = ([01X]{36})$', line)
            if match:
                mask = match.group(1)
                continue

            match = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            if match:
                address = int(match.group(1))
                value = '{0:036b}'.format(int(match.group(2)))
                result = self.do_mask1(value, mask)
                memory[address] = int(result, 2)

        return sum(memory.values())

    def part2(self):
        memory = {}
        for line in self.lines:
            match = re.match(r'^mask = ([01X]{36})$', line)
            if match:
                mask = match.group(1)
                continue

            match = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            if match:
                address = '{0:036b}'.format(int(match.group(1)))
                value = int(match.group(2))
                result = self.do_mask2(address, mask)
                x = [i for i in range(len(result)) if result[-i-1] == 'X']
                for n in range(pow(2, len(x))):
                    mask1 = self.make_mask1(x, n)
                    address = self.do_mask1(result, mask1)
                    memory[address] = value

        return sum(memory.values())


def main():
    inputs = open("day14.txt").read().strip()
    day14 = Day14(inputs)
    print(f'Part 1: {day14.part1()}')
    print(f'Part 2: {day14.part2()}')


if __name__ == "__main__":
    main()
