import os
import math

os.chdir(os.path.dirname(__file__))


def _distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.hypot(x2 - x1, y2 - y1, z2 - z1)


def input():
    input = open("input.txt").read().strip()
    boxes = [tuple(map(int, line.split(","))) for line in input.split("\n")]

    distances = {}
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            box1 = boxes[i]
            box2 = boxes[j]
            dist = _distance(box1, box2)
            distances[dist] = set([box1, box2])

    return boxes, distances


def part1():
    boxes, distances = input()
    circuits = [{box} for box in boxes]
    close = sorted(distances.keys())

    for i in range(1000):
        box1, box2 = distances[close[i]]
        circuit = set()

        for box in [box1, box2]:
            for c in circuits:
                if box in c:
                    circuit |= c
                    circuits.remove(c)

        circuits.append(circuit)

    circuits = sorted(circuits, key=lambda c: len(c))
    produce = math.prod([len(c) for c in circuits[-3:]])

    print("part1:", produce)


def part2():
    boxes, distances = input()
    circuits = [{box} for box in boxes]
    close = sorted(distances.keys())

    for i in range(len(close)):
        box1, box2 = distances[close[i]]
        circuit = set()

        for box in [box1, box2]:
            for c in circuits:
                if box in c:
                    circuit |= c
                    circuits.remove(c)

        circuits.append(circuit)
        if len(circuits) == 1:
            break

    print("part2:", box1[0] * box2[0])


part1()
part2()
