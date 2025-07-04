import os

os.chdir(os.path.dirname(__file__))


def input():
    section1, section2 = open("input.txt").read().split("\n\n")
    rules = [[int(page) for page in line.split("|")] for line in section1.split()]
    updates = [[int(page) for page in line.split(",")] for line in section2.split()]
    return rules, updates


def part1():
    rules, updates = input()

    numbers = []
    for update in updates:
        for rule in rules:
            try:
                if update.index(rule[0]) >= update.index(rule[1]):
                    break
            except:
                continue
        else:
            numbers.append(update[int(len(update) / 2)])

    print(sum(numbers))


def part2():
    pass


part1()
part2()
