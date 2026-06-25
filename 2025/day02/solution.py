import os

os.chdir(os.path.dirname(__file__))


def _bound_upper(num: int) -> int:
    """当前数量级范围的上限"""
    digits = len(str(num))
    return 10**digits - 1


def input() -> list[str]:
    input = open("input.txt").read().strip()
    ranges = []

    for field in input.split(","):
        first, last = map(int, field.split("-"))
        upper = _bound_upper(first)

        if upper < last:
            ranges.append((first, upper))
            ranges.append((upper + 1, last))
        else:
            ranges.append((first, last))

    return ranges


def part1():
    invalid = []

    for first, last in input():
        digits = len(str(first))

        if digits % 2 != 0:
            continue

        half = int(str(first)[: int(digits / 2)])

        while True:
            id = int(str(half) * 2)
            if id > last:
                break
            if id >= first:
                invalid.append(id)

            half += 1

    print("part1: ", sum(invalid))


def part2():
    invalid = set()

    for first, last in input():
        digits = len(str(first))

        for d in range(1, int(digits / 2) + 1):
            if digits % d != 0:
                continue

            times = int(digits / d)
            root = int(str(first)[:d])

            while True:
                id = int(str(root) * times)
                if id > last:
                    break
                if id >= first:
                    invalid.add(id)
                root += 1

    print("part2: ", sum(invalid))


part1()
part2()
