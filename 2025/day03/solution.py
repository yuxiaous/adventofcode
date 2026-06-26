import os

os.chdir(os.path.dirname(__file__))


def input() -> list[str]:
    input = open("input.txt").read().strip()
    lines = [line.strip() for line in input.split("\n")]
    banks = [tuple(int(joltage) for joltage in list(batteries)) for batteries in lines]
    return banks


def part1():
    joltages = []

    for bank in input():
        tens = max(bank[:-1])
        index = bank.index(tens)
        ones = max(bank[index + 1 :])
        largest = tens * 10 + ones
        joltages.append(largest)

    print("part1: ", sum(joltages))


part1()
