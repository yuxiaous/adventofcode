import os
from math import prod

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read()
    worksheet = [list(row) for row in input.split("\n")]
    problems = []

    start = 0
    while True:
        for end in range(start, len(worksheet[0])):
            for r in range(len(worksheet)):
                if worksheet[r][end] != " ":
                    break
            else:
                problem = [worksheet[r][start:end] for r in range(len(worksheet))]
                problems.append(problem)
                start = end + 1
                break
        else:
            problem = [worksheet[r][start:] for r in range(len(worksheet))]
            problems.append(problem)
            break

    return problems


def part1():
    problems = input()
    results = []

    for problem in problems:
        symbol = "".join(problem[-1]).strip()
        numbers = [int("".join(num)) for num in problem[:-1]]

        if symbol == "+":
            results.append(sum(numbers))
        elif symbol == "*":
            results.append(prod(numbers))

    print("part1:", sum(results))


def part2():
    problems = input()
    results = []

    for problem in problems:
        symbol = "".join(problem[-1]).strip()
        numbers = [int("".join(num)) for num in list(zip(*problem[:-1]))]

        if symbol == "+":
            results.append(sum(numbers))
        elif symbol == "*":
            results.append(prod(numbers))

    print("part2:", sum(results))

    pass


part1()
part2()
