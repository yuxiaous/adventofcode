import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    sections = input.split("\n\n")
    patterns = [x for x in sections[0].split(", ")]
    designs = [x for x in sections[1].split("\n")]
    return patterns, designs


def part1():
    patterns, designs = input()
    impossible = set()

    def arrangeable(design, patterns):
        if design in impossible:
            return False

        for pattern in patterns:
            if design[: len(pattern)] == pattern:
                next = design[len(pattern) :]
                if not next:
                    return True
                if arrangeable(next, patterns):
                    return True

        impossible.add(design)
        return False

    count = 0
    for design in designs:
        if arrangeable(design, patterns):
            count += 1
    print(count)


part1()
