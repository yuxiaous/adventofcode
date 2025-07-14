import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    return [int(n) for n in input.split(" ")]


def part1():
    numbers = input()

    for _ in range(25):
        old = numbers
        numbers = []
        for n in old:
            if n == 0:
                numbers.append(1)
                continue

            nstr = str(n)
            if len(nstr) % 2 == 0:
                numbers.append(int(nstr[: len(nstr) // 2]))
                numbers.append(int(nstr[len(nstr) // 2 :]))
                continue

            numbers.append(n * 2024)

    print(len(numbers))


def part2():
    numbers = input()
    counts = {}

    def record(n, c):
        if n in counts:
            counts[n] += c
        else:
            counts[n] = c

    for n in numbers:
        record(n, 1)

    for _ in range(75):
        old = counts
        counts = {}
        for n, c in old.items():
            if n == 0:
                record(1, c)
                continue

            nstr = str(n)
            if len(nstr) % 2 == 0:
                record(int(nstr[: len(nstr) // 2]), c)
                record(int(nstr[len(nstr) // 2 :]), c)
                continue

            record(n * 2024, c)

    print(sum(counts.values()))


part1()
part2()
