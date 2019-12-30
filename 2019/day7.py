#!/usr/bin/env python3

from itertools import permutations
from computer import Intcode

# test1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
# test2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
# test3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
# test4 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
# test5 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'

class Day7:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def configure(self, phases):
        self.amplifiers = []
        for i in range(len(phases)):
            amp = Intcode(self.codes)
            amp.input(phases[i])
            self.amplifiers.append(amp)

    def _series(self, signal):
        for amp in self.amplifiers:
            if amp.status == Intcode.HALT:
                return False, signal
            while True:
                status = amp.run()
                if status == Intcode.INPUT:
                    amp.input(signal)
                elif status == Intcode.OUTPUT:
                    signal = amp.output()
                    break
                elif status == Intcode.HALT:
                    break
        return True, signal

    def _loop(self, signal):
        goon = True
        while goon:
            goon, signal = self._series(signal)
        return signal

    def find_largest(self, setting):
        signals = []
        for phases in list(permutations(setting)):
            self.configure(phases)
            signal = self._loop(0)
            signals.append((signal, phases))
        return max(signals)

    def part1(self):
        return self.find_largest([0, 1, 2, 3, 4])

    def part2(self):
        return self.find_largest([5, 6, 7, 8, 9])

def main():
    program = open('day7.txt').read().strip()
    day7 = Day7(program)
    print(f'Part 1: {day7.part1()}')
    print(f'Part 2: {day7.part2()}')

if __name__ == "__main__":
    main()
