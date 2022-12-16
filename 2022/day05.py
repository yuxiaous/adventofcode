#!/usr/bin/env python3
import re

input = [x for x in open("day05.txt").read().split("\n\n")]


def parse_stacks(input: str) -> dict[int, list]:
    lines = input.split("\n")
    lines.reverse()
    index = lines[0]
    crates = lines[1:]
    stacks = {}

    for i in range(len(index)):
        if index[i] != " ":
            idx = int(index[i])
            stacks[idx] = [c[i] for c in crates if c[i] != " "]

    return stacks


def parse_procedure(input: str):
    steps = input.split("\n")
    procedure = []

    for step in steps:
        match = re.match(r"^move (\d+) from (\d+) to (\d+)$", step)
        procedure.append(tuple(int(x) for x in match.groups()))

    return procedure


class CrateMover9000:
    def move(self, stacks: dict[int, list], step):
        quantity = step[0]
        frm = step[1]
        to = step[2]
        for _ in range(quantity):
            crate = stacks[frm].pop()
            stacks[to].append(crate)


class CrateMover9001:
    def move(self, stacks: dict[int, list], step):
        quantity = step[0]
        frm = step[1]
        to = step[2]

        moved = stacks[frm][-quantity:]
        stacks[frm] = stacks[frm][:-quantity]
        stacks[to].extend(moved)


def part1():
    stacks = parse_stacks(input[0])
    procedure = parse_procedure(input[1])
    crane = CrateMover9000()

    for step in procedure:
        crane.move(stacks, step)

    return "".join(x[-1] for x in stacks.values())


def part2():
    stacks = parse_stacks(input[0])
    procedure = parse_procedure(input[1])
    crane = CrateMover9001()

    for step in procedure:
        crane.move(stacks, step)

    return "".join(x[-1] for x in stacks.values())


if __name__ == "__main__":
    print("--- Day 5: Supply Stacks ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
