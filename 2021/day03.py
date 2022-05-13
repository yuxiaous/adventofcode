#!/usr/bin/env python3

input = open('day03.txt').read().strip().split('\n')


def consider(numbers, position, criteria):
    bits = [x[position] for x in numbers]
    if criteria == 'most':
        return '1' if bits.count('1') >= bits.count('0') else '0'
    elif criteria == 'least':
        return '0' if bits.count('0') <= bits.count('1') else '1'


def part1(input):
    def calculate(criteria):
        rate = ''
        for i in range(len(input[0])):
            rate += consider(input, i, criteria)
        return int(rate, 2)

    gamma_rate = calculate('most')
    epsilon_rate = calculate('least')
    return gamma_rate * epsilon_rate


def part2(input):
    def search(criteria):
        numbers = [x for x in input]
        for i in range(len(input[0])):
            bit = consider(numbers, i, criteria)
            numbers = [x for x in numbers if x[i] == bit]
            if len(numbers) == 1:
                break
        return int(numbers[0], 2)

    oxygen_generator_rating = search('most')
    CO2_scrubber_rating = search('least')
    return oxygen_generator_rating * CO2_scrubber_rating


if __name__ == '__main__':
    print('--- Day 3: Binary Diagnostic ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
