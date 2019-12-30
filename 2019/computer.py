#!/usr/bin/env python3

class Intcode:
    NEXT = 0
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99
    INVALID = -1

    def __init__(self, codes):
        self.status = Intcode.NEXT
        self.memory = {i: x for i, x in enumerate(codes)}
        self.pointer = 0
        self.inputs = []
        self.outputs = []

    def set_noun_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb
    
    def input(self, value):
        self.status = Intcode.NEXT
        self.inputs.append(value)

    def output(self):
        self.status = Intcode.NEXT
        return self.outputs.pop(0)

    def _parse(self, value):
        v = format(value, '05')
        opcode = int(v[3:5])
        mode1 = int(v[2:3])
        mode2 = int(v[1:2])
        mode3 = int(v[0:1])
        return opcode, [mode1, mode2, mode3]

    def _read(self, param, mode):
        # position mode
        if mode == 0:
            return self.memory[param]
        # immediate mode
        elif mode == 1:
            return param

    def _write(self, param, mode, value):
        # position mode
        if mode == 0:
            self.memory[param] = value

    def _instruction_add(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        value3 = value1 + value2
        self._write(param3, modes[2], value3)
        self.pointer += 4
        return Intcode.NEXT

    def _instruction_multiply(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        value3 = value1 * value2
        self._write(param3, modes[2], value3)
        self.pointer += 4
        return Intcode.NEXT

    def _instruction_input(self, modes):
        if len(self.inputs) > 0:
            param1 = self.memory[self.pointer + 1]
            value1 = self.inputs.pop(0)
            self._write(param1, modes[0], value1)
            self.pointer += 2
            return Intcode.NEXT
        else:
            return Intcode.INPUT

    def _instruction_output(self, modes):
        param1 = self.memory[self.pointer + 1]
        value1 = self._read(param1, modes[0])
        self.outputs.append(value1)
        self.pointer += 2
        return Intcode.OUTPUT

    def _instruction_jump_if_true(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        if value1 != 0:
            self.pointer = value2
        else:
            self.pointer += 3
        return Intcode.NEXT

    def _instruction_jump_if_false(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        if value1 == 0:
            self.pointer = value2
        else:
            self.pointer += 3
        return Intcode.NEXT

    def _instruction_less_than(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        self._write(param3, modes[2], 1 if value1 < value2 else 0)
        self.pointer += 4
        return Intcode.NEXT

    def _instruction_equals(self, modes):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self._read(param1, modes[0])
        value2 = self._read(param2, modes[1])
        self._write(param3, modes[2], 1 if value1 == value2 else 0)
        self.pointer += + 4
        return Intcode.NEXT

    def _run_instruction(self):
        opcode, modes = self._parse(self.memory[self.pointer])
        if opcode == Intcode.ADD:
            return self._instruction_add(modes)
        elif opcode == Intcode.MULTIPLY:
            return self._instruction_multiply(modes)
        elif opcode == Intcode.INPUT:
            return self._instruction_input(modes)
        elif opcode == Intcode.OUTPUT:
            return self._instruction_output(modes)
        elif opcode == Intcode.JUMP_IF_TRUE:
            return self._instruction_jump_if_true(modes)
        elif opcode == Intcode.JUMP_IF_FALSE:
            return self._instruction_jump_if_false(modes)
        elif opcode == Intcode.LESS_THAN:
            return self._instruction_less_than(modes)
        elif opcode == Intcode.EQUALS:
            return self._instruction_equals(modes)
        elif opcode == Intcode.HALT:
            return Intcode.HALT
        return Intcode.INVALID

    def run(self):
        while self.status == Intcode.NEXT:
            self.status = self._run_instruction()
        return self.status
