#!/usr/bin/env python3

rucksacks = [x for x in open("day03.txt").read().strip().split("\n")]


def get_prioritie(item):
    if "a" <= item <= "z":
        return ord(item) - 96
    elif "A" <= item <= "Z":
        return ord(item) - 38
    return 0


def part1():
    priorities = []
    for items in rucksacks:
        half = int(len(items) / 2)
        compartment1 = items[:half]
        compartment2 = items[half:]

        def find_share():
            for type1 in compartment1:
                for type2 in compartment2:
                    if type1 == type2:
                        return type1

        share = find_share()
        prioritie = get_prioritie(share)
        priorities.append(prioritie)

    return sum(priorities)


def part2():
    priorities = []
    for i in range(0, len(rucksacks), 3):
        rucksack1 = rucksacks[i]
        rucksack2 = rucksacks[i + 1]
        rucksack3 = rucksacks[i + 2]

        def find_share():
            for type1 in rucksack1:
                for type2 in rucksack2:
                    for type3 in rucksack3:
                        if type1 == type2 == type3:
                            return type1

        share = find_share()
        prioritie = get_prioritie(share)
        priorities.append(prioritie)

    return sum(priorities)


if __name__ == "__main__":
    print("--- Day 3: Rucksack Reorganization ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
