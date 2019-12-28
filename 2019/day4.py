#!/usr/bin/env python3

def six_digit(digits):
    return len(digits) == 6

def same_adjacent_digits(digits):
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False

def not_part_of_larger(digits):
    # [i-1] != [i] == [i+1] != [i+2]
    for i in range(len(digits) - 1):
        if (i == 0 or digits[i - 1] != digits[i]) and digits[i] == digits[i + 1] and (i >= 4 or digits[i + 1] != digits[i + 2]):
            return True
    return False

def never_decrease(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

def is_meet_criteria(password, part):
    digits = [int(digit) for digit in str(password)]

    # Six-digit number
    if not six_digit(digits):
        return False
    # Two adjacent digits are the same
    if part == 1 and not same_adjacent_digits(digits):
        return False
    # Not part of a larger group of matching digits
    elif part == 2 and not not_part_of_larger(digits):
        return False
    # The digits never decrease
    if not never_decrease(digits):
        return False

    return True

def main():
    with open('day4.txt') as f:
        values = f.read().strip().split('-')
        rule_range = [int(value) for value in values]

        def part(id):
            count = 0
            for password in range(rule_range[0], rule_range[1] + 1):
                if is_meet_criteria(password, id):
                    count += 1
            return count

        # Part1
        print("Part 1:", part(1))
        # Part2
        print("Part 2:", part(2))

if __name__ == "__main__":
    main()
