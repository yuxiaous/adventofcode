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


class Keypad:
    def __init__(self, layout):
        self.keypad = layout

        self.buttons = {}
        for y in range(len(layout)):
            for x in range(len(layout[0])):
                if layout[y][x] != "#":
                    self.buttons[layout[y][x]] = (x, y)

        self.moves = {}
        for btn1 in self.buttons:
            for btn2 in self.buttons:
                x1, y1 = self.buttons[btn1]
                x2, y2 = self.buttons[btn2]

                sequences = set()

                # 先横后竖
                if x1 != x2 and self.keypad[y1][x2] != "#":
                    sequences.add(
                        (">" if x2 > x1 else "<") * abs(x2 - x1)
                        + ("v" if y2 > y1 else "^") * abs(y2 - y1)
                    )

                # 先竖后横
                if y1 != y2 and self.keypad[y2][x1] != "#":
                    sequences.add(
                        ("v" if y2 > y1 else "^") * abs(y2 - y1)
                        + (">" if x2 > x1 else "<") * abs(x2 - x1)
                    )

                self.moves[(btn1, btn2)] = sequences or set({""})

    def type(self, code):
        def _type(code, i):
            if i >= len(code):
                return set({""})

            btn1 = code[i - 1] if i > 0 else "A"
            btn2 = code[i]
            seq1 = self.moves[(btn1, btn2)]
            seq2 = _type(code, i + 1)
            return set(s1 + "A" + s2 for s1 in seq1 for s2 in seq2)

        return _type(code, 0)


def part1():
    codes = input()

    def operate(keypad: Keypad, codes):
        sequences = set()
        for code in codes:
            sequences = set.union(sequences, keypad.type(code))
        return sequences

    complexity = []
    for code in codes:
        sequences0 = [code]
        sequences1 = operate(Keypad(keypad1), sequences0)
        sequences2 = operate(Keypad(keypad2), sequences1)
        sequences3 = operate(Keypad(keypad2), sequences2)

        length = min([len(s) for s in sequences3])
        ncode = int(code[:-1])
        complexity.append(length * ncode)

    print(sum(complexity))


part1()
