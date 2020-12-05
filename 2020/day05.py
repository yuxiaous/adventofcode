#!/usr/bin/env python3

class Seat:
    def __init__(self, seat):
        self.seat = seat

        # rows
        region = [0, 127]
        for i in range(0, 7):
            half = (region[1] - region[0] + 1) / 2
            character = self.seat[i]
            if character == 'F':
                region[1] -= half
            elif character == 'B':
                region[0] += half
        self.row = int(region[0])

        # columns
        region = [0, 7]
        for i in range(7, 10):
            half = (region[1] - region[0] + 1) / 2
            character = self.seat[i]
            if character == 'L':
                region[1] -= half
            elif character == 'R':
                region[0] += half
        self.column = int(region[0])

        # seat ID
        self.seat_id = self.row * 8 + self.column


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
