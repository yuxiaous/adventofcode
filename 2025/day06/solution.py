import os
from math import prod

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    numbers = [list(map(int, lines[i].split())) for i in range(len(lines) - 1)]
    symbols = lines[-1].split()
    problems = []
    
    for i in range(len(symbols)):
        problem = []
        for j in range(len(numbers)):
            problem.append(numbers[j][i])
        problem.append(symbols[i])

        problems.append(problem)

    return problems


def part1():
    problems = input()
    results = []

    for problem in problems:
        numbers = problem[:-1]
        symbol = problem[-1]

        if symbol == "+":
            results.append(sum(numbers))
        elif symbol == "*":
            results.append(prod(numbers))

    print("part1: ", sum(results))


part1()
