#!/usr/bin/env python3

input = open('day24.txt').read().strip()
# print(input)
input = input.split('\n')


class ArithmeticLogicUnit:
    def __init__(self):
        self.variables = {}
        self.variables['w'] = 0
        self.variables['x'] = 0
        self.variables['y'] = 0
        self.variables['z'] = 0
        self.inputs = []

    def inp(self, a):
        value = self.inputs[0]
        self.inputs.pop(0)
        if type(value) == int:
            self.variables[a] = value
        else:
            self.variables[a] = int(value)

    def add(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] + b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] + int(b)
        else:
            self.variables[a] = self.variables[a] + self.variables[b]

    def mul(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] * b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] * int(b)
        else:
            self.variables[a] = self.variables[a] * self.variables[b]

    def div(self, a, b):
        if type(b) == int:
            self.variables[a] = int(self.variables[a] / b)
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = int(self.variables[a] / int(b))
        else:
            self.variables[a] = int(self.variables[a] / self.variables[b])

    def mod(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] % b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] % int(b)
        else:
            self.variables[a] = self.variables[a] % self.variables[b]

    def eql(self, a, b):
        if type(b) == int:
            self.variables[a] = 1 if self.variables[a] == b else 0
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = 1 if self.variables[a] == int(b) else 0
        else:
            self.variables[a] = 1 if self.variables[a] == self.variables[b] else 0

    def execute(self, instruction: str):
        cmd = instruction.split()
        op = cmd[0]
        if op == 'inp':
            self.inp(cmd[1])
        elif op == 'add':
            self.add(cmd[1], cmd[2])
        elif op == 'mul':
            self.mul(cmd[1], cmd[2])
        elif op == 'div':
            self.div(cmd[1], cmd[2])
        elif op == 'mod':
            self.mod(cmd[1], cmd[2])
        elif op == 'eql':
            self.eql(cmd[1], cmd[2])


class Program:
    def __init__(self, input):
        self.instructions = [x for x in input]
        self.index = 0

    def run(self, alu: ArithmeticLogicUnit):
        while self.index < len(self.instructions):
            instruction = self.instructions[self.index]
            alu.execute(instruction)
            self.index += 1


def part1(input: str):
    alu = ArithmeticLogicUnit()

    model = [1, 2, 9, 9, 6, 9, 9, 7, 8, 2, 9, 3, 9, 9]

    for w in model:
        alu.inputs.append(w)

    xlist = []
    ylist = []
    zlist = []
    for i in range(14):
        length = 18
        start = length * i
        end = start + length
        program = Program(input[start:end])
        program.run(alu)
        xlist.append(alu.variables['x'])
        ylist.append(alu.variables['y'])
        zlist.append(alu.variables['z'])
    # print(xlist)
    # print(ylist)
    # print(zlist)
    return ''.join([str(x) for x in model])


# inp w
# mul x 0
# add x z
# mod x 26
# div z (a)
# add x (b)
# eql x w
# eql x 0    x = (z % 26) + b    !=    w
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y (c)
# mul y x
# add z y    z = (z / a) * (25 * x + 1) + (w + c) * x


def part2(input):
    alu = ArithmeticLogicUnit()

    model = [1, 1, 8, 4, 1, 2, 3, 1, 1, 1, 7, 1, 8, 9]

    for w in model:
        alu.inputs.append(w)

    xlist = []
    ylist = []
    zlist = []
    for i in range(14):
        length = 18
        start = length * i
        end = start + length
        program = Program(input[start:end])
        program.run(alu)
        xlist.append(alu.variables['x'])
        ylist.append(alu.variables['y'])
        zlist.append(alu.variables['z'])
    # print(xlist)
    # print(ylist)
    # print(zlist)

    return ''.join([str(x) for x in model])


if __name__ == '__main__':
    print('--- Day 24: Arithmetic Logic Unit ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
