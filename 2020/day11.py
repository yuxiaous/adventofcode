#!/usr/bin/env python3

class QuickMap:
    def __init__(self, layout, part):
        self.layout = layout
        self.seats = [[seat for seat in row]
                      for row in self.layout.split('\n')]
        self.width = len(self.seats[0])
        self.height = len(self.seats)
        self.part = part

    def apply(self, row, col):
        if self.part == 1:
            radius = range(1, 2)
            accept = 4
        elif self.part == 2:
            radius = range(1, 100)
            accept = 5

        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for direction in directions:
            for r in radius:
                offset = [x * r for x in direction]
                pos = [sum(x) for x in zip((row, col), offset)]
                if pos[0] < 0 or pos[0] >= self.height or pos[1] < 0 or pos[1] >= self.width:
                    break
                seat = self.seats[pos[0]][pos[1]]
                if seat == 'L':
                    break
                if seat == '#':
                    count += 1
                    break

        seat = self.seats[row][col]
        if seat == 'L' and count == 0:
            return '#'
        if seat == '#' and count >= accept:
            return 'L'

    def round(self):
        seats = [row[:] for row in self.seats]
        for row in range(self.height):
            for col in range(self.width):
                seat = self.apply(row, col)
                if seat:
                    seats[row][col] = seat
        self.seats = seats
        return ''.join([''.join(row) for row in self.seats])

    def stabilize(self):
        last = ''
        count = 0
        while True:
            now = self.round()
            if now == last:
                break
            last = now

            count += 1
            print(count, end='\r')

        count = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    count += 1
        return count

    def display(self):
        for row in self.seats:
            print(''.join(row))


class Day11:
    def __init__(self, inputs):
        self.layout = inputs
        pass

    def part1(self):
        qmap = QuickMap(self.layout, 1)
        return qmap.stabilize()

    def part2(self):
        qmap = QuickMap(self.layout, 2)
        return qmap.stabilize()


def main():
    inputs = open("day11.txt").read().strip()
    day11 = Day11(inputs)
    print(f'Part 1: {day11.part1()}')
    print(f'Part 2: {day11.part2()}')


if __name__ == "__main__":
    main()
