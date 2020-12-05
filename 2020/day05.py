#!/usr/bin/env python3

class Seat:
    def __init__(self, seat):
        self.seat = seat
        # rows
        self.row = self.parse([0, 127], range(0, 7), 'F', 'B')
        # columns
        self.column = self.parse([0, 7], range(7, 10), 'L', 'R')
        # seat ID
        self.seat_id = self.row * 8 + self.column

    def parse(self, region, range, lower, upper):
        for i in range:
            half = (region[1] - region[0] + 1) / 2
            character = self.seat[i]
            if character == lower:
                region[1] -= half
            elif character == upper:
                region[0] += half
        return int(region[0])


class Day5:
    def __init__(self, inputs):
        self.seats = [Seat(x) for x in inputs.split('\n')]
        self.seats.sort(key=lambda s: s.seat_id)

    def part1(self):
        return self.seats[-1].seat_id

    def part2(self):
        for i in range(len(self.seats) - 1):
            front = self.seats[i].seat_id
            back = self.seats[i + 1].seat_id
            if back != front + 1:
                return front + 1


def main():
    inputs = open('day05.txt').read().strip()
    day5 = Day5(inputs)
    print(f'Part 1: {day5.part1()}')
    print(f'Part 2: {day5.part2()}')


if __name__ == "__main__":
    main()
