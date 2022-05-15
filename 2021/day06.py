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
    pass


if __name__ == '__main__':
    print('--- Day 6: Lanternfish ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
