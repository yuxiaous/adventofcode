#!/usr/bin/env python3

import computer

def main():
    with open('day2.txt') as f:
        program = f.read().strip()
        codes = [int(x) for x in program.split(',')]

        # Part 1
        computer1 = computer.Intcode(codes)
        computer1.set_noun_verb(12, 2)
        computer1.run()
        print("Part1:", computer1.memory[0])

        # Part 2
        output = 19690720
        for noun in range(0, 100):
            for verb in range(0, 100):
                computer2 = computer.Intcode(codes)
                computer2.set_noun_verb(noun, verb)
                computer2.run()
                if computer2.memory[0] == output:
                    print("Part2:", 100 * noun + verb)

if __name__ == "__main__":
    main()