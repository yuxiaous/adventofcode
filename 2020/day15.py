#!/usr/bin/env python3


class Day15:
    def __init__(self, inputs):
        self.numbers = [int(x) for x in inputs.split(',')]

    def play(self, over):
        turn = len(self.numbers)
        spoken = {}
        for i in range(turn):
            number = self.numbers[i]
            spoken[number] = i + 1

        turn += 1
        current = 0
        while turn < over:
            number = current
            if current in spoken:
                current = turn - spoken[current]
            else:
                current = 0
            spoken[number] = turn
            turn += 1
            print(f'{round(turn/over*100, 2)}%', end='\r')
        return current

    def part1(self):
        return self.play(2020)

    def part2(self):
        return self.play(30000000)


def main():
    inputs = open("day15.txt").read().strip()
    day15 = Day15(inputs)
    print(f'Part 1: {day15.part1()}')
    print(f'Part 2: {day15.part2()}')


if __name__ == "__main__":
    main()
