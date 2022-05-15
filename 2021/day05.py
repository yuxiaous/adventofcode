#!/usr/bin/env python3

input = open('day05.txt').read().strip().split('\n')


class CoordinateSystem:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.coordinates = [[0 for i in range(h)] for j in range(w)]

    def draw_line(self, end1, end2):
        x1, y1 = end1
        x2, y2 = end2

        if x1 == x2:
            y1, y2 = (y2, y1) if y1 > y2 else (y1, y2)
            for y in range(y1, y2+1):
                x = x1
                self.coordinates[x][y] += 1

        elif y1 == y2:
            x1, x2 = (x2, x1) if x1 > x2 else (x1, x2)
            for x in range(x1, x2+1):
                y = y1
                self.coordinates[x][y] += 1

    def get_overlap_number(self):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.coordinates[x][y] > 1:
                    count += 1
        return count


def parse_entry(entry: str):
    ends = entry.split(' -> ')
    end1 = tuple(int(x) for x in ends[0].split(','))
    end2 = tuple(int(x) for x in ends[1].split(','))
    return (end1, end2)


def part1(input):
    coor = CoordinateSystem(1000, 1000)
    for entry in input:
        end1, end2 = parse_entry(entry)
        coor.draw_line(end1, end2)
    return coor.get_overlap_number()


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 5: Hydrothermal Venture ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
