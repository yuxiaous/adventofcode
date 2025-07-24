import os
import math

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    lines = input.split("\n")
    RegisterA = int(lines[0][12:])
    RegisterB = int(lines[1][12:])
    RegisterC = int(lines[2][12:])
    Porgram = [int(x) for x in lines[4][9:].split(",")]
    return RegisterA, RegisterB, RegisterC, Porgram


class Computer:
    def __init__(self, A=0, B=0, C=0):
        self.registerA = A
        self.registerB = B
        self.registerC = C
        self.pointer = 0
        self.output = []

    def literal(self, operand):
        return operand

    def combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.registerA
        elif operand == 5:
            return self.registerB
        elif operand == 6:
            return self.registerC

    def instruction(self, opcode, operand):
        # adv
        if opcode == 0:
            self.registerA = int(self.registerA / 2 ** self.combo(operand))
        # bxl
        elif opcode == 1:
            self.registerB = self.registerB ^ self.literal(operand)
        # bst
        elif opcode == 2:
            self.registerB = self.combo(operand) % 8
        # jnz
        elif opcode == 3:
            if self.registerA != 0:
                self.pointer = self.literal(operand)
                return 0
        # bxc
        elif opcode == 4:
            self.registerB = self.registerB ^ self.registerC
        # out
        elif opcode == 5:
            self.output.append(self.combo(operand) % 8)
        # bdv
        elif opcode == 6:
            self.registerB = int(self.registerA / 2 ** self.combo(operand))
        # cdv
        elif opcode == 7:
            self.registerC = int(self.registerA / 2 ** self.combo(operand))
        return 2

    def execute(self, program):
        while self.pointer < len(program):
            opcode = program[self.pointer]
            operand = program[self.pointer + 1]
            increase = self.instruction(opcode, operand)
            self.pointer += increase

    def print(self):
        out = ",".join(map(str, self.output))
        print(out)


def part1():
    a, b, c, program = input()
    computer = Computer(a, b, c)
    computer.execute(program)
    computer.print()


part1()


def part2():
    a, b, c, program = input()
    a = 0

    length = len(program) - 1
    while True:
        increment = int("1" + "0" * length, 8)
        a += increment

        computer = Computer(a, b, c)
        computer.execute(program)

        for i in range(len(program)):
            if computer.output[-i - 1] != program[-i - 1]:
                length = len(program) - i - 1
                break
        else:
            break

    print(a)


part2()
