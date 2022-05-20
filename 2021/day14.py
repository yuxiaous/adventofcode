#!/usr/bin/env python3

input = open('day14.txt').read().strip()


def map_add(m, k, v):
    if k in m:
        m[k] += v
    else:
        m[k] = v


def part1(input):
    entries = input.split('\n\n')
    polymer = entries[0]
    rules = {x[0]: x[1]
             for x in [x.split(' -> ') for x in entries[1].split('\n')]}

    for _ in range(10):
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
        map_add(elements, c, 1)

    _, most = max(elements.items(), key=lambda x: x[1])
    _, lease = min(elements.items(), key=lambda x: x[1])
    return most - lease


def part2(input):
    entries = input.split('\n\n')
    template = entries[0]
    rules = {x[0]: x[1]
             for x in [x.split(' -> ') for x in entries[1].split('\n')]}

    pairs = {}
    pairs[template[0]] = 1
    pairs[template[-1]] = 1
    for i in range(len(template)-1):
        pair = template[i:i+2]
        map_add(pairs, pair, 1)

    for _ in range(40):
        copy = pairs
        pairs = {}
        for pair in copy:
            if pair in rules:
                e = rules[pair]
                map_add(pairs, pair[0] + e, copy[pair])
                map_add(pairs, e + pair[1], copy[pair])
            else:
                pairs[pair] = copy[pair]

    elements = {}
    for pair in pairs:
        for c in pair:
            map_add(elements, c, pairs[pair] / 2)

    _, most = max(elements.items(), key=lambda x: x[1])
    _, lease = min(elements.items(), key=lambda x: x[1])
    return int(most - lease)


if __name__ == '__main__':
    print('--- Day 14: Extended Polymerization ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
