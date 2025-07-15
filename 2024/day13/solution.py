import os
import re
from typing import Dict

os.chdir(os.path.dirname(__file__))


def input():
    machines = []
    input = open("input.txt").read().strip()
    for machine in input.split("\n\n"):
        A = re.search(r"Button A: X\+(\d+), Y\+(\d+)", machine)
        B = re.search(r"Button B: X\+(\d+), Y\+(\d+)", machine)
        P = re.search(r"Prize: X=(\d+), Y=(\d+)", machine)
        machines.append(
            {
                "A": tuple(int(x) for x in A.groups()),
                "B": tuple(int(x) for x in B.groups()),
                "P": tuple(int(x) for x in P.groups()),
            }
        )
    return machines


def part1():
    token = 0
    for machine in input():
        ax, ay = machine["A"]
        bx, by = machine["B"]
        px, py = machine["P"]
        times_a = (by * px - bx * py) / (ax * by - ay * bx)
        times_b = (ax * py - ay * px) / (ax * by - ay * bx)
        if times_a % 1 == 0 and times_b % 1 == 0:
            token += int(times_a) * 3 + int(times_b) * 1
    print(token)


part1()
