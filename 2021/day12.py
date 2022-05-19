#!/usr/bin/env python3

input = open('day12.txt').read().strip().split('\n')


def make_caves_map(input):
    def connect_caves(c1, c2):
        if c1 == 'end':
            return
        if c2 == 'start':
            return
        if c1 in caves_map:
            caves_map[c1].append(c2)
        else:
            caves_map[c1] = [c2]

    caves_map = {}
    for entry in input:
        c1, c2 = entry.split('-')
        connect_caves(c1, c2)
        connect_caves(c2, c1)
    return caves_map


def part1(input):
    caves_map = make_caves_map(input)
    paths = []
    next = [['start']]
    while len(next) > 0:
        copy = next
        next = []
        for path in copy:
            last = path[-1]
            for cave in caves_map[last]:
                if cave == 'end':
                    paths.append(path + [cave])
                elif cave.isupper() or cave not in path:
                    next.append(path + [cave])
    return len(paths)


def part2(input):
    caves_map = make_caves_map(input)
    paths = []
    next = [[0, 'start']]
    while len(next) > 0:
        copy = next
        next = []
        for path in copy:
            last = path[-1]
            for cave in caves_map[last]:
                if cave == 'end':
                    paths.append(path + [cave])
                elif cave.isupper() or cave not in path:
                    next.append(path + [cave])
                elif cave in path and path[0] < 1:
                    next.append(path + [cave])
                    next[-1][0] += 1
    return len(paths)


if __name__ == '__main__':
    print('--- Day 12: Passage Pathing ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
