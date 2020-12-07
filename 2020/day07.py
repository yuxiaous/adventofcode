#!/usr/bin/env python3

import re


class Day7:
    def __init__(self, inputs):
        self.rules_text = [rule for rule in inputs.split('\n')]
        self.rules_map = {}
        for rule in self.rules_text:
            bags = re.findall(r'(\d+ )?(\w+ \w+) bags?', rule)

            key = bags[0][1]
            contains = {}
            for bag in bags[1:]:
                if bag[0]:
                    contains[bag[1]] = int(bag[0])

            self.rules_map[key] = contains

    def part1(self):
        targets = {'shiny gold'}

        colors = set()
        while True:
            contains = set()
            for color in targets:
                for bag in self.rules_map:
                    if color in self.rules_map[bag]:
                        contains.add(bag)
            colors |= contains
            targets = contains

            if not targets:
                break

        return len(colors)

    def part2(self):
        def contains(bag):
            count = 0
            bags = self.rules_map[bag]
            for bag in bags:
                num = bags[bag]
                count += num + num * contains(bag)
            return count

        return contains('shiny gold')


def main():
    inputs = open('day07.txt').read().strip()
    day7 = Day7(inputs)
    print(f'Part 1: {day7.part1()}')
    print(f'Part 2: {day7.part2()}')


if __name__ == "__main__":
    main()
