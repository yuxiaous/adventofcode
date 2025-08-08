import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    sections = input.split("\n\n")

    wires = {
        wire: value == "1"
        for line in sections[0].split("\n")
        for wire, value in [line.split(": ")]
    }
    gates = {
        output: (gate, input1, input2)
        for line in sections[1].split("\n")
        for inputs, output in [line.split(" -> ")]
        for input1, gate, input2 in [inputs.split(" ")]
    }

    return wires, gates


GATE = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a ^ b,
}


def part1():
    wires, gates = input()

    def output(wire):
        if wire not in gates and wire in wires:
            return wires[wire]
        gate, input1, input2 = gates[wire]
        return GATE[gate](output(input1), output(input2))

    binary = ""
    for wire in sorted(filter(lambda w: w.startswith("z"), gates.keys()), reverse=True):
        binary += "1" if output(wire) else "0"
    print(int(binary, 2))


part1()
