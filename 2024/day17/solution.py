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
    def __init__(self, init=(0, 0, 0, [])):
        self.registerA = init[0]
        self.registerB = init[1]
        self.registerC = init[2]
        self.program = init[3]
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
            if self.registerA:
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

    def execute(self, program=None):
        if not program:
            program = self.program

        while self.pointer < len(program):
            opcode = program[self.pointer]
            operand = program[self.pointer + 1]
            increase = self.instruction(opcode, operand)
            self.pointer += increase

    def print(self):
        out = ",".join(map(str, self.output))
        print(out)


def part1():
    computer = Computer(input())
    computer.execute()
    computer.print()


part1()
