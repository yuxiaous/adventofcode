import os
import math

os.chdir(os.path.dirname(__file__))


def input() -> list[str]:
    lines = open("input.txt").readlines()
    return [line.strip() for line in lines]


def part1():
    point = 50
    count = 0

    for rotation in input():
        turn = rotation[0]
        distance = int(rotation[1:])

        if turn == "L":
            point -= distance
        elif turn == "R":
            point += distance

        if point % 100 == 0:
            count += 1

    print("part1: ", count)


def _floor100(x: int) -> int:
    """向下取整到100的倍数"""
    return int(math.floor(float(x) / 100) * 100)


def _ceil100(x: int) -> int:
    """向上取整到100的倍数"""
    return int(math.ceil(float(x) / 100) * 100)


def part2():
    point = 50
    count = 0

    for rotation in input():
        turn = rotation[0]
        distance = int(rotation[1:])

        if turn == "L":
            while True:
                gap = point - (_ceil100(point) - 100)  # 向下求差距
                if gap <= distance:
                    point -= gap
                    distance -= gap
                    count += 1
                else:
                    point -= distance
                    distance = 0
                    break

        elif turn == "R":
            while True:
                gap = (_floor100(point) + 100) - point  # 向上求差距
                if gap <= distance:
                    point += gap
                    distance -= gap
                    count += 1
                else:
                    point += distance
                    distance = 0
                    break

    print("part2: ", count)


part1()
part2()
