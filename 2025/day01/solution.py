import os

os.chdir(os.path.dirname(__file__))


def input() -> list[str]:
    lines = open("input.txt").readlines()
    return [line.strip() for line in lines]


def rotate_dial(initial: int, rotation: str) -> int:
    turn = rotation[0]
    distance = int(rotation[1:])
    point = initial

    if turn == "L":
        point -= distance
    elif turn == "R":
        point += distance

    while point < 0:
        point += 100
    while point > 99:
        point -= 100

    return point


def part1():
    point = 50
    count = 0

    for rotation in input():
        point = rotate_dial(point, rotation)
        if point == 0:
            count += 1

    print("part1: ", count)


def part2():
    pass


part1()
part2()
