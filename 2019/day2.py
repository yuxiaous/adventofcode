#!/usr/bin/env python3

class IntcodeComputer:
    def __init__(self, codes):
        self.memory = {i: x for i, x in enumerate(codes)}
        self.pointer = 0

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

    def set_noun_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

def main():
    with open('day2.txt') as f:
        program = f.read().strip()
        codes = [int(x) for x in program.split(',')]

    # Part 1
    computer1 = IntcodeComputer(codes)
    computer1.set_noun_verb(12, 2)
    computer1.run()
    print("Part1:", computer1.memory[0])

    # Part 2
    output = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            computer2 = IntcodeComputer(codes)
            computer2.set_noun_verb(noun, verb)
            computer2.run()
            if computer2.memory[0] == output:
                print("Part2:", 100 * noun + verb)

if __name__ == "__main__":
    main()