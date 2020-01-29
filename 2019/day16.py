#!/usr/bin/env python3

test1 = '80871224585914546619083218645595'
test2 = '19617804207202209144916044189917'
test3 = '69317163492948606335995924319873'

class Day16:
    def __init__(self, signal):
        self.signal = [int(digit) for digit in signal]
        self.pattern = [0, 1, 0, -1]

    def FFT(self, signal, pattern, phases):
        output = signal
        for _ in range(phases):
            inputs = output
            output = []
            for n in range(len(inputs)):
                digit = 0
                for i in range(len(inputs)):
                    p = int((i+1) / (n+1)) % len(pattern)
                    digit += inputs[i] * pattern[p]
                digit = abs(digit) % 10
                output.append(digit)
        return output

    def part1(self):
        output = self.FFT(self.signal, self.pattern, 100)
        return ''.join(str(d) for d in output[:8])

    def part2(self):
        pass

def main():
    signal = open('day16.txt').read().strip()
    day16 = Day16(signal)
    print(f'Part 1: {day16.part1()}')
    print(f'Part 2: {day16.part2()}')

if __name__ == "__main__":
    main()
