#!/usr/bin/env python3


class Circle:
    def __init__(self, values):
        self.values = {i: values[i] for i in range(len(values))}
        self.size = len(self.values)

    def __key(self, key):
        while key < 0:
            key += self.size
        while key >= self.size:
            key -= self.size
        return key

    def __getitem__(self, key):
        return self.values[self.__key(key)]

    def __setitem__(self, key, value):
        self.values[self.__key(key)] = value

    def __delitem__(self, key):
        del self.values[self.__key(key)]

    def __len__(self):
        return self.size

    def __str__(self):
        return f'{[self.values[i] for i in range(self.size) if i in self.values]}'

    def __contains__(self, item):
        return item in self.values.values()

    def index(self, element):
        for i in range(self.size):
            if self.values[i] == element:
                return i

    def min(self):
        return min(self.values.values())

    def max(self):
        return max(self.values.values())


class Game:
    def __init__(self, values):
        self.cups = Circle(values)
        self.current = self.cups[0]
        self.destination = None
        self.count = 0

    def move(self):
        self.count += 1
        print(f'-- move {self.count} --')
        print(f'cups: {self.cups} ({self.current})')

        current_index = self.cups.index(self.current)

        # 1. picks up the three cups
        picks = []
        index = current_index
        for _ in range(3):
            index += 1
            picks.append(self.cups[index])
            del self.cups[index]
        print(f'pick up: {picks}')

        # 2. selects a destination cup
        destination = self.current
        while True:
            destination -= 1
            if destination < self.cups.min():
                destination = self.cups.max()
            if destination in self.cups:
                self.destination = destination
                break
        print(f'destination: {self.destination}')

        # 3. places the cups just picked up immediately clockwise of the destination cup
        index = current_index
        while True:
            index += 1
            self.cups[index] = self.cups[index + 3]
            del self.cups[index + 3]
            if self.cups[index] == self.destination:
                break
        for i in range(3):
            index += 1
            self.cups[index] = picks[i]

        # 4. selects a new current cup
        self.current = self.cups[current_index + 1]
        print('')

    def play(self, times):
        for _ in range(times):
            self.move()

        print('-- final --')
        print(f'cups: {self.cups} ({self.current})')


class Day23:
    def __init__(self, inputs):
        self.cups = [int(x) for x in list(inputs)]

    def part1(self):
        game = Game(self.cups)
        game.play(100)

        labels = []
        index = game.cups.index(1)
        for _ in range(len(game.cups) - 1):
            index += 1
            labels.append(str(game.cups[index]))
        return ''.join(labels)

    def part2(self):
        pass


def main():
    inputs = open("day23.txt").read().strip()
    day23 = Day23(inputs)
    print(f'Part 1: {day23.part1()}')
    print(f'Part 2: {day23.part2()}')


if __name__ == "__main__":
    main()
