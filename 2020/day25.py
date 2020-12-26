#!/usr/bin/env python3

class Device:
    def __init__(self, subject_number):
        self.subject_number = subject_number
        self.loop_size = None

    def __transform(self, number):
        assert(self.loop_size != None)

        value = 1
        for _ in range(self.loop_size):
            value *= number
            value %= 20201227
        return value

    def encryption_key(self, subject_number):
        return self.__transform(subject_number)

    def reverse_engineer(self, public_key):
        value = 1
        loop = 0
        while True:
            loop += 1
            value *= 7
            value %= 20201227
            if value == public_key:
                self.loop_size = loop
                return loop


class Day25:
    def __init__(self, inputs):
        self.public_keys = [int(x) for x in inputs.split('\n')]

    def part1(self):
        device = Device(7)
        device.reverse_engineer(self.public_keys[1])
        return device.encryption_key(self.public_keys[0])

    def part2(self):
        pass


def main():
    inputs = open("day25.txt").read().strip()
    day25 = Day25(inputs)
    print(f'Part 1: {day25.part1()}')
    print(f'Part 2: {day25.part2()}')


if __name__ == "__main__":
    main()
