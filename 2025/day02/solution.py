import os

os.chdir(os.path.dirname(__file__))


def input() -> list[str]:
    input = open("input.txt").read().strip()
    ranges = [tuple(int(id) for id in part.split("-")) for part in input.split(",")]
    return ranges


def part1():
    invalid = []

    for r in input():
        first = r[0]
        last = r[1]

        first_str = str(first)
        half_str = first_str[: int(len(first_str) / 2)]
        if half_str == "":
            half = 0
        else:
            half = int(half_str)

        while True:
            id = int(str(half) * 2)
            if id > last:
                break
            if id >= first:
                invalid.append(id)

            half += 1

    print("part1: ", sum(invalid))


part1()
