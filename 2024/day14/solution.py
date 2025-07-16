import os
import re
from functools import reduce

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()

    robots = []
    for robot in input.split("\n"):
        match = re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", robot)
        robot = tuple(int(x) for x in match.groups())
        robots.append(robot)
    return robots


def move(robot, w, h):
    px, py = robot[0], robot[1]
    vx, vy = robot[2], robot[3]
    px += vx
    py += vy
    while px < 0:
        px += w
    while px >= w:
        px -= w
    while py < 0:
        py += h
    while py >= h:
        py -= h
    return (px, py, vx, vy)


def part1():
    robots = input()
    w = max(r[0] + 1 for r in robots)
    h = max(r[1] + 1 for r in robots)

    for _ in range(100):
        for i in range(len(robots)):
            robots[i] = move(robots[i], w, h)

    count = [0] * 4
    for robot in robots:
        x, y = robot[0], robot[1]

        if 0 <= x < w // 2 and 0 <= y < h // 2:
            count[0] += 1
        if w // 2 < x < w and 0 <= y < h // 2:
            count[1] += 1
        if 0 <= x < w // 2 and h // 2 < y < h:
            count[2] += 1
        if w // 2 < x < w and h // 2 < y < h:
            count[3] += 1

    print(reduce(lambda x, y: x * y, count))


part1()
