#!/usr/bin/env python3

import re

input = open('day13.txt').read().strip()


class TransparentPaper:
    def __init__(self, dots):
        self.dots = set(tuple(int(x) for x in dot.split(',')) for dot in dots)

    def fold(self, instruction):
        m = re.match('fold along ([xy])=(\d+)', instruction)
        fold = m.group(1)
        pos = int(m.group(2))

        if fold == 'y':
            for x, y in set(self.dots):
                if y > pos:
                    self.dots.remove((x, y))
                    self.dots.add((x, pos * 2 - y))
        elif fold == 'x':
            for x, y in set(self.dots):
                if x > pos:
                    self.dots.remove((x, y))
                    self.dots.add((pos * 2 - x, y))

    def show(self):
        max_x = max([dot[0] for dot in self.dots])
        max_y = max([dot[1] for dot in self.dots])
        for y in range(max_y+1):
            for x in range(max_x+1):
                if (x, y) in self.dots:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')


def part1(input):
    dots, instructions = input.split('\n\n')

    dots = dots.split('\n')
    instructions = instructions.split('\n')

    paper = TransparentPaper(dots)
    paper.fold(instructions[0])
    return len(paper.dots)


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 13: Transparent Origami ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
