#!/usr/bin/env python3

input = open('day20.txt').read().strip()


class Image:
    def __init__(self, original: str):
        original = original.split('\n')

        self.pixels = {}
        self.width = len(original[0])
        self.height = len(original)
        self.background = '.'

        for r in range(self.height):
            for c in range(self.width):
                pixel = original[r][c]
                self.pixels[(r, c)] = pixel

    def enhance(self, algorithm):
        def enhance_pixel(pixels: str):
            pixels = pixels.replace('#', '1')
            pixels = pixels.replace('.', '0')
            index = int(pixels, 2)
            return algorithm[index]

        image = {}
        for r in range(-1, self.height+1):
            for c in range(-1, self.width+1):
                square = []
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if (i, j) in self.pixels:
                            square.append(self.pixels[(i, j)])
                        else:
                            square.append(self.background)
                pixel = enhance_pixel(''.join(square))
                image[(r+1, c+1)] = pixel

        self.pixels = image
        self.width += 2
        self.height += 2
        self.background = enhance_pixel(self.background * 9)

    def show(self):
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) in self.pixels:
                    print(self.pixels[(r, c)], end='')
                else:
                    print('.', end='')
            print('')


def part1(input: str):
    sections = input.split('\n\n')
    algorithm = [x for x in sections[0].replace('\n', '')]

    image = Image(sections[1])
    image.enhance(algorithm)
    image.enhance(algorithm)

    count = 0
    for pixel in image.pixels.values():
        if pixel == '#':
            count += 1
    return count


def part2(input):
    sections = input.split('\n\n')
    algorithm = [x for x in sections[0].replace('\n', '')]

    image = Image(sections[1])
    for i in range(50):
        image.enhance(algorithm)

    count = 0
    for pixel in image.pixels.values():
        if pixel == '#':
            count += 1
    return count


if __name__ == '__main__':
    print('--- Day 20: Trench Map ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
