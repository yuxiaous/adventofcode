#!/usr/bin/env python3

import re


class Day19:
    def __init__(self, inputs):
        inputs = inputs.split('\n\n')
        # rule
        self.rules = {}
        for rule in inputs[0].split('\n'):
            m = re.match(r'(\d+): (.+)', rule)
            self.rules[m.group(1)] = m.group(2).replace('"', '')
        # message
        self.messages = [x for x in inputs[1].split('\n')]

    def part1(self):
        pattern = self.rules['0']
        while m := re.search(r'(\d+)', pattern):
            pattern = pattern[:m.start()] + \
                f'({self.rules[m.group(0)]})' + \
                pattern[m.end():]
        pattern = pattern.replace(' ', '')

        count = 0
        for message in self.messages:
            m = re.match('^' + pattern + '$', message)
            if m:
                count += 1
        return count

    def part2(self):
        self.rules['8'] = '(42)+'
        self.rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31'
        return self.part1()


def main():
    inputs = open("day19.txt").read().strip()
    day19 = Day19(inputs)
    print(f'Part 1: {day19.part1()}')
    print(f'Part 2: {day19.part2()}')


if __name__ == "__main__":
    main()
