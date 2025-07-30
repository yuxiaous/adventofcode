import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    codes = input.split("\n")
    return codes


keypad1 = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"],
]

keypad2 = [
    ["#", "^", "A"],
    ["<", "v", ">"],
]


class Robot:
    def __init__(self, keypad):
        self.keypad = keypad

    def find(self, btn):
        h, w = len(self.keypad), len(self.keypad[0])
        for y in range(h):
            for x in range(w):
                if self.keypad[y][x] == btn:
                    return (x, y)

    def move(self, fr, to):
        x1, y1 = self.find(fr)
        x2, y2 = self.find(to)

        sequences = []
        tracks = {(x1, y1): ""}
        while tracks:
            (x, y), path = tracks.popitem()

            if x == x2 and y == y2:
                sequences.append(path)
                continue

            if x2 > x and self.keypad[y][x + 1] != "#":
                tracks[(x + 1, y)] = path + ">"
            if x2 < x and self.keypad[y][x - 1] != "#":
                tracks[(x - 1, y)] = path + "<"
            if y2 > y and self.keypad[y + 1][x] != "#":
                tracks[(x, y + 1)] = path + "v"
            if y2 < y and self.keypad[y - 1][x] != "#":
                tracks[(x, y - 1)] = path + "^"
        return sequences

    def type(self, code):
        sequences = []
        for i in range(len(code)):
            fr = code[i - 1] if i > 0 else "A"
            to = code[i]

            previous = sequences
            sequences = []
            for sequence in self.move(fr, to):
                if previous:
                    for pre in previous:
                        sequences.append(pre + sequence + "A")
                else:
                    sequences.append(sequence + "A")

        return sequences


def part1():
    codes = input()

    def operate(robot: Robot, codes):
        sequences = []

        for code in codes:
            sequences += robot.type(code)

        shortest = min(len(s) for s in sequences)
        sequences = list(filter(lambda x: len(x) <= shortest, sequences))
        return sequences

    complexity = []
    for code in codes:
        sequences0 = [code]
        sequences1 = operate(Robot(keypad1), sequences0)
        sequences2 = operate(Robot(keypad2), sequences1)
        sequences3 = operate(Robot(keypad2), sequences2)

        length = len(sequences3[0])
        ncode = int(code[:-1])
        complexity.append(length * ncode)

    print(sum(complexity))


part1()
