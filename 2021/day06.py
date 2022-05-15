#!/usr/bin/env python3

input = open('day06.txt').read().strip().split(',')


def part1(input):
    fish = [int(x) for x in input]

    for day in range(80):
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] += 7
                fish.append(8)
    return len(fish)


def part2(input):
    fish = {}
    for x in input:
        f = int(x)
        if f in fish:
            fish[f] += 1
        else:
            fish[f] = 1

    for day in range(256):
        copy = dict(fish)
        fish = {x: 0 for x in range(9)}
        for f, n in copy.items():
            f -= 1
            if f < 0:
                f += 7
                fish[8] += n
            fish[f] += n

    return sum(fish.values())


if __name__ == '__main__':
    print('--- Day 6: Lanternfish ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
