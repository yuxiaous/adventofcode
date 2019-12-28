#!/usr/bin/env python3

class Intcode:
    def __init__(self, codes):
        self.memory = {i: x for i, x in enumerate(codes)}
        self.pointer = 0

    def set_noun_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

    def _instruction_add(self):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self.memory[param1]
        value2 = self.memory[param2]
        value3 = value1 + value2
        self.memory[param3] = value3
        self.pointer += 4

    def _instruction_multiply(self):
        param1 = self.memory[self.pointer + 1]
        param2 = self.memory[self.pointer + 2]
        param3 = self.memory[self.pointer + 3]
        value1 = self.memory[param1]
        value2 = self.memory[param2]
        value3 = value1 * value2
        self.memory[param3] = value3
        self.pointer += 4

    def _run_instruction(self):
        opcode = self.memory[self.pointer]
        if opcode == 1:
            self._instruction_add()
            return True
        elif opcode == 2:
            self._instruction_multiply()
            return True
        elif opcode == 99:
            return False
        return False

    def run(self):
        while True:
            res = self._run_instruction()
            if not res:
                break
