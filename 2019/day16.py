#!/usr/bin/env python3

test1 = '80871224585914546619083218645595'
test2 = '19617804207202209144916044189917'
test3 = '69317163492948606335995924319873'
test4 = '03036732577212944063491565474664'
test5 = '02935109699940807407585447034323'
test6 = '03081770884921959731165446850517'

class Day16:
    def __init__(self, signal):
        self.signal = [int(digit) for digit in signal]
        self.pattern = [0, 1, 0, -1]

    def FFT(self, signal, pattern, phases):
        length = len(signal)
        output = signal
        for k in range(phases):
            print(f'{k}/{phases}', end='\r')
            inputs = output
            output = []
            for n in range(length):
                digit = 0
                for i in range(length):
                    p = int((i+1) / (n+1)) % len(pattern)
                    digit += inputs[i] * pattern[p]
                digit = abs(digit) % 10
                output.append(digit)
        return output

    def decode_message(self, signal):
        phases = 100
        times = 10000
        offset = int(''.join(str(digit) for digit in signal[:7]))

        # Make real signal fragment from offset to end
        real = []
        for i in range(offset, len(signal) * times):
            index = i % len(signal)
            real.append(signal[index])

        # Decode signal 
        length = len(real)
        output = real
        for k in range(phases):
            print(f'{k}/{phases}', end='\r')
            inputs = output
            output = [0] * length
            digit = 0
            for n in range(length):
                index = length - n - 1
                digit = inputs[index] + digit
                digit = abs(digit) % 10
                output[index] = digit
        return ''.join(str(d) for d in output[:8])

    def part1(self):
        output = self.FFT(self.signal, self.pattern, 100)
        return ''.join(str(d) for d in output[:8])

    def part2(self):
        return self.decode_message(self.signal)

def main():
    signal = open('day16.txt').read().strip()
    day16 = Day16(signal)
    print(f'Part 1: {day16.part1()}')
    print(f'Part 2: {day16.part2()}')

if __name__ == "__main__":
    main()
