#!/usr/bin/env python3

import re

class Day2:
    def __init__(self, inputs):
        self.passwords = []
        for line in inputs.split('\n'):
            match = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
            password = {
                'first': int(match.group(1)),
                'second': int(match.group(2)),
                'letter': match.group(3),
                'password': match.group(4)
            }
            # print(password)
            self.passwords.append(password)

    def part1(self):
        count = 0
        for p in self.passwords:
            lowest = p['first']
            highest = p['second']
            times = p['password'].count(p['letter'])
            if times >= lowest and times <= highest:
                count += 1
        return count

    def part2(self):
        count = 0
        for p in self.passwords:
            letter1 = p['password'][p['first'] - 1]
            letter2 = p['password'][p['second'] - 1]
            given = p['letter']
            if (letter1 == given) ^ (letter2 == given):
                count += 1
        return count

def main():
    inputs = open('day02.txt').read().strip()
    day2 = Day2(inputs)
    print(f'Part 1: {day2.part1()}')
    print(f'Part 2: {day2.part2()}')

if __name__ == "__main__":
    main()
