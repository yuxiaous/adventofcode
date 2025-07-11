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


part1()
