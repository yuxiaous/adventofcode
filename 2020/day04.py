#!/usr/bin/env python3

import re


class Passport:
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional = ['cid']

    def __init__(self, data):
        self.fields = {}

        for field in data.split():
            kv = field.split(':')
            key = kv[0]
            value = kv[1]
            self.fields[key] = value

    def is_valid(self, part):
        for key in self.required:
            if key not in self.fields:
                return False
            if part == 2 and not self.validate(key):
                return False
        return True

    def validate(self, key):
        if key == 'byr':
            value = int(self.fields[key])
            return value >= 1920 and value <= 2002
        if key == 'iyr':
            value = int(self.fields[key])
            return value >= 2010 and value <= 2020
        if key == 'eyr':
            value = int(self.fields[key])
            return value >= 2020 and value <= 2030
        if key == 'hgt':
            value = self.fields[key]
            match = re.match(r'^(\d+)(cm|in)$', value)
            if match == None:
                return False
            hgt = int(match.group(1))
            unit = match.group(2)
            if unit == 'cm':
                return hgt >= 150 and hgt <= 193
            if unit == 'in':
                return hgt >= 59 and hgt <= 76
        if key == 'hcl':
            value = self.fields[key]
            return re.match(r'^#[0-9a-f]{6}$', value) != None
        if key == 'ecl':
            value = self.fields[key]
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if key == 'pid':
            value = self.fields[key]
            return re.match(r'^[0-9]{9}$', value) != None
        return False


class Day4:
    def __init__(self, inputs):
        self.passports = [Passport(data) for data in inputs.split('\n\n')]

    def part1(self):
        count = 0
        for passport in self.passports:
            if passport.is_valid(1):
                count += 1
        return count

    def part2(self):
        count = 0
        for passport in self.passports:
            if passport.is_valid(2):
                count += 1
        return count


def main():
    inputs = open('day04.txt').read().strip()
    day4 = Day4(inputs)
    print(f'Part 1: {day4.part1()}')
    print(f'Part 2: {day4.part2()}')


if __name__ == "__main__":
    main()
