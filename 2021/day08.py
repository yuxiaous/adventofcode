#!/usr/bin/env python3

input = open('day08.txt').read().strip().split('\n')


def part1(input):
    count = 0
    for entry in input:
        for output in entry.split('|')[1].split():
            if len(output) in (2, 3, 4, 7):
                count += 1
    return count


def part2(input):
    sum = 0

    for entry in input:
        patterns = {x: None for x in entry.split('|')[0].split()}
        digits = {x: None for x in range(10)}

        # determine 1, 4, 7, 8
        for pattern in patterns:
            if len(pattern) == 2:
                patterns[pattern] = 1
                digits[1] = set(pattern)
            elif len(pattern) == 3:
                patterns[pattern] = 7
                digits[7] = set(pattern)
            elif len(pattern) == 4:
                patterns[pattern] = 4
                digits[4] = set(pattern)
            elif len(pattern) == 7:
                patterns[pattern] = 8
                digits[8] = set(pattern)
        # determine 2, 3, 6, 9
        for pattern in patterns:
            if len(pattern) == 5:
                if len(set(pattern) | digits[4]) == 7:
                    patterns[pattern] = 2
                    digits[2] = set(pattern)
                elif len(set(pattern) | digits[1]) == 5:
                    patterns[pattern] = 3
                    digits[3] = set(pattern)
            elif len(pattern) == 6:
                if len(set(pattern) | digits[1]) == 7:
                    patterns[pattern] = 6
                    digits[6] = set(pattern)
                elif len(set(pattern) | digits[4]) == 6:
                    patterns[pattern] = 9
                    digits[9] = set(pattern)
        # determine 0, 5
        for pattern in patterns:
            if len(pattern) == 5:
                if set(pattern) not in (digits[2], digits[3]):
                    patterns[pattern] = 5
                    digits[5] = set(pattern)
            elif len(pattern) == 6:
                if set(pattern) not in (digits[6], digits[9]):
                    patterns[pattern] = 0
                    digits[0] = set(pattern)

        # decode output value
        value = 0
        for output in entry.split('|')[1].split():
            for digit, segments in digits.items():
                if set(output) == segments:
                    value *= 10
                    value += digit
                    break

        # add all output values
        sum += value

    return sum


if __name__ == '__main__':
    print('--- Day 8: Seven Segment Search ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
