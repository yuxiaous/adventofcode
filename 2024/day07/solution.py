import os

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").read().strip().split("\n")
    equations = dict()
    for line in lines:
        value, numbers = line.split(": ")
        equations[int(value)] = [int(n) for n in numbers.split(" ")]
    return equations


def part1():
    total = 0
    for value, numbers in input().items():
        results = set({numbers[0]})
        for i in range(1, len(numbers)):
            pre = results
            results = set()
            for num in pre:
                results.add(num + numbers[i])
                results.add(num * numbers[i])
        if value in results:
            total += value

    print(total)


def part2():
    total = 0
    for value, numbers in input().items():
        results = set({numbers[0]})
        for i in range(1, len(numbers)):
            pre = results
            results = set()
            for num in pre:
                results.add(num + numbers[i])
                results.add(num * numbers[i])
                results.add(int(str(num) + str(numbers[i])))
        if value in results:
            total += value

    print(total)


part1()
part2()
