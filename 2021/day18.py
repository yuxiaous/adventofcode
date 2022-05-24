#!/usr/bin/env python3
import math

input = open('day18.txt').read().strip().split('\n')


class SnailfishNumber:
    def __init__(self, entry=None):
        self.number: int = None
        self.left: SnailfishNumber = None
        self.right: SnailfishNumber = None
        if entry:
            self._parse(entry)

    def _parse(self, entry):
        index = 0

        def do(sn: SnailfishNumber):
            nonlocal index
            open = None
            split = None
            close = None
            child = None

            while True:
                if entry[index] == '[':
                    if open is None:
                        open = index
                    else:
                        child = do(SnailfishNumber())
                elif entry[index] == ',':
                    split = index
                    if child:
                        sn.left = child
                        child = None
                    else:
                        sn.left = SnailfishNumber()
                        sn.left.number = int(entry[open+1:split])
                elif entry[index] == ']':
                    close = index
                    if child:
                        sn.right = child
                        child = None
                    else:
                        sn.right = SnailfishNumber()
                        sn.right.number = int(entry[split+1:close])
                    break
                index += 1
            return sn
        sn = do(self)
        sn._reduce()

    def _reduce(self):
        while True:
            if self._explode():
                continue
            if self._split():
                continue
            break

    def _explode(self):
        order = []
        target = None

        def do(sn: SnailfishNumber, level=0):
            nonlocal order
            nonlocal target
            if sn.number is not None:
                order.append(sn)
            if sn.left:
                do(sn.left, level+1)
            if sn.right:
                do(sn.right, level+1)
            if (level >= 4 and not target
                and sn.left and sn.left.number is not None
                and sn.right and sn.right.number is not None
                ):
                target = (sn.left, sn.right)
                sn.left = None
                sn.right = None
                sn.number = 0
        do(self)

        if target:
            left, right = target
            index = order.index(left)
            if index > 0:
                order[index-1].number += left.number
            index = order.index(right)
            if index < len(order) - 1:
                order[index+1].number += right.number
            return True
        return False

    def _split(self):
        action = False

        def do(sn: SnailfishNumber):
            nonlocal action
            if not action and sn.number is not None and sn.number >= 10:
                action = True
                sn.left = SnailfishNumber()
                sn.left.number = math.floor(sn.number/2)
                sn.right = SnailfishNumber()
                sn.right.number = math.ceil(sn.number/2)
                sn.number = None
            if sn.left:
                do(sn.left)
            if sn.right:
                do(sn.right)
        do(self)
        return action

    def __add__(self, other):
        parent = SnailfishNumber()
        parent.left = self
        parent.right = other
        parent._reduce()
        return parent

    def magnitude(self):
        def do(sn: SnailfishNumber):
            if sn.number is not None:
                return sn.number

            left = None
            right = None
            if sn.left:
                left = do(sn.left)
            if sn.right:
                right = do(sn.right)
            return left * 3 + right * 2

        return do(self)

    def __str__(self):
        def do(sn: SnailfishNumber):
            if sn.left is None or sn.right is None:
                return sn.number
            return [do(sn.left), do(sn.right)]
        return do(self).__str__()


def part1(input):
    sum = SnailfishNumber(input[0])
    for entry in input[1:]:
        sum += SnailfishNumber(entry)
    return sum.magnitude()


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 18: Snailfish ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
