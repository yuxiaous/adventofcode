#!/usr/bin/env python3


input = open('day04.txt').read().strip().split('\n\n')
drawn_numbers = [int(x) for x in input[0].split(',')]


class BingoBoard:
    ROW = 5
    COLUMN = 5

    def __init__(self, numbers):
        self.numbers = [int(x) for x in numbers]
        self.marked = [False for _ in numbers]

    def mark(self, number):
        # mark number
        for i in range(len(self.numbers)):
            if self.numbers[i] == number:
                self.marked[i] = True

        # check win
        for r in range(self.ROW):
            win = True
            for c in range(self.COLUMN):
                win &= self.marked[r * self.ROW + c]
            if win:
                return True
        for c in range(self.COLUMN):
            win = True
            for r in range(self.ROW):
                win &= self.marked[r * self.ROW + c]
            if win:
                return True
        return False

    def get_unmarked_numbers(self):
        numbers = []
        for i in range(len(self.marked)):
            if not self.marked[i]:
                numbers.append(self.numbers[i])
        return numbers


def part1(input):
    boards = [BingoBoard(x.split()) for x in input[1:]]
    for number in drawn_numbers:
        for board in boards:
            if board.mark(number):
                unmarked = board.get_unmarked_numbers()
                return sum(unmarked) * number


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 4: Giant Squid ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
