import os

os.chdir(os.path.dirname(__file__))


def input():
    lines = open("input.txt").readlines()
    return [[int(n) for n in line.split()] for line in lines]


def is_safe(report):
    order = report[-1] - report[0]
    if order > 0:
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if diff < 1 or diff > 3:
                return False
    elif order < 0:
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if diff > -1 or diff < -3:
                return False
    else:
        return False
    return True


def part1():
    count = 0
    for report in input():
        if is_safe(report):
            count += 1
    print(count)


def part2():
    count = 0
    for report in input():
        if is_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    count += 1
                    break
    print(count)


part1()
part2()
