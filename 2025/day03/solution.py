import os

os.chdir(os.path.dirname(__file__))


def input():
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


def part2():
    joltages = []

    limit = 12
    for bank in input():
        largest = 0

        start = 0
        for end in range(len(bank) + 1 - limit, len(bank) + 1):
            digit = max(bank[start:end])
            start = bank.index(digit, start, end) + 1
            largest = largest * 10 + digit

        joltages.append(largest)

    print("part2: ", sum(joltages))


part1()
part2()
