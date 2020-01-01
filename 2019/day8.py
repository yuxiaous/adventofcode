#!/usr/bin/env python3

import io

class SpaceImage:
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2

    def __init__(self, digits, wide, tall):
        self.wide = wide
        self.tall = tall
        square = wide * tall
        self.layers = [digits[square*i:square*(i+1)] for i in range(int(len(digits)/square))]

    def looks(self):
        square = self.wide * self.tall
        looks = [SpaceImage.TRANSPARENT] * square
        
        for layer in self.layers:
            for i in range(len(layer)):
                if looks[i] == SpaceImage.TRANSPARENT:
                    looks[i] = layer[i]

        return looks

class Day8:
    def __init__(self, data):
        self.digits = [int(digit) for digit in list(data)]

    def part1(self):
        image = SpaceImage(self.digits, 25, 6)
        layer = min(image.layers, key=lambda l: l.count(0))
        return layer.count(1) * layer.count(2)

    def part2(self):
        image = SpaceImage(self.digits, 25, 6)
        looks = image.looks()

        with io.StringIO() as stream:
            for r in range(image.tall):
                stream.write('\n')
                for c in range(image.wide):
                    pixel = looks[image.wide * r + c]
                    if pixel == SpaceImage.WHITE:
                        stream.write('■')
                    else:
                        stream.write(' ')

            return stream.getvalue()

def main():
    data = open('day8.txt').read().strip()
    day8 = Day8(data)
    print(f'Part 1: {day8.part1()}')
    print(f'Part 2: {day8.part2()}')

if __name__ == "__main__":
    main()
