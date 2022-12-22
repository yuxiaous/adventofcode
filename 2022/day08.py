#!/usr/bin/env python3

input = open("day08.txt").read().strip()

map = [[int(c) for c in r] for r in input.split("\n")]


def part1():
    visible = 2 * len(map) + 2 * len(map[0]) - 4

    for r in range(1, len(map) - 1):
        for c in range(1, len(map[r]) - 1):
            given = map[r][c]
            directions = [
                [map[x][c] for x in range(0, r)],  # up
                [map[x][c] for x in range(r + 1, len(map))],  # down
                [map[r][x] for x in range(0, c)],  # left
                [map[r][x] for x in range(c + 1, len(map[r]))],  # right
            ]

            for direction in directions:
                if given > max(direction):
                    visible += 1
                    break

    return visible


def part2():
    highest = 0

    for r in range(1, len(map) - 1):
        for c in range(1, len(map[r]) - 1):
            given = map[r][c]
            directions = [
                [map[x][c] for x in reversed(range(0, r))],  # up
                [map[x][c] for x in range(r + 1, len(map))],  # down
                [map[r][x] for x in reversed(range(0, c))],  # left
                [map[r][x] for x in range(c + 1, len(map[r]))],  # right
            ]

            score = 1
            for direction in directions:
                view = 0
                for tree in direction:
                    view += 1
                    if tree >= given:
                        break
                score *= view

            if score > highest:
                highest = score

    return highest


if __name__ == "__main__":
    print("--- Day 8: Treetop Tree House ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
