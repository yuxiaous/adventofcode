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

    for output, (gate, input1, input2) in gates.items():
        if input1 not in wires:
            wires[input1] = None
        if input2 not in wires:
            wires[input2] = None
        if output not in wires:
            wires[output] = None
    return wires, gates


GATE = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a ^ b,
}


def part1():
    wires, gates = input()
    z_valid = {wire: False for wire in wires.keys() if wire.startswith("z")}

    while not all(z_valid.values()):
        for wire, value in wires.items():
            if value != None:
                continue

            gate, input1, input2 = gates[wire]

            if wires[input1] == None or wires[input2] == None:
                continue

            wires[wire] = GATE[gate](wires[input1], wires[input2])

            if wire.startswith("z"):
                z_valid[wire] = True

    binary = ""
    for wire in sorted(filter(lambda w: w.startswith("z"), wires.keys()), reverse=True):
        binary += "1" if wires[wire] else "0"
    print(int(binary, 2))


part1()
