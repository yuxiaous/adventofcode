#!/usr/bin/env python3

input = open('day14.txt').read().strip()


def parse(input):
    entries = input.split('\n\n')
    template = entries[0]
    pairs = [x.split(' -> ') for x in entries[1].split('\n')]
    rules = {x[0]: x[1] for x in pairs}
    return template, rules


def part1(input):
    polymer, rules = parse(input)
    for i in range(10):
        copy = polymer
        polymer = ''
        for i in range(len(copy)):
            polymer += copy[i]
            if i < len(copy) - 1:
                pair = copy[i:i+2]
                if pair in rules:
                    polymer += rules[pair]

    elements = {}
    for c in polymer:
        if c in elements:
            elements[c] += 1
        else:
            elements[c] = 1

    _, most = max(elements.items(), key=lambda x: x[1])
    _, lease = min(elements.items(), key=lambda x: x[1])
    return most - lease


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 14: Extended Polymerization ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
