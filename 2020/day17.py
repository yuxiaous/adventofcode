#!/usr/bin/env python3

class PocketDimension:
    def __init__(self, initial, dimension):
        self.dimension = dimension
        self.actives = set(cube + (0,) * (dimension - len(cube))
                           for cube in initial if initial[cube] == '#')
        self.turn = 0

    def neighbors(self, cube):
        assert(len(cube) == self.dimension)

        neighbors = [()]
        for _ in range(self.dimension):
            neighbors = [x + (j,) for j in [-1, 0, 1] for x in neighbors]
        neighbors.remove(self.dimension * (0,))
        neighbors = set(tuple(map(sum, zip(cube, neighbor)))
                        for neighbor in neighbors)
        return neighbors

    def is_active(self, cube):
        count = 0
        for neighbor in self.neighbors(cube):
            if neighbor in self.actives:
                count += 1
        if cube in self.actives:
            if count == 2 or count == 3:
                return True
        else:
            if count == 3:
                return True
        return False

    def cycle(self):
        self.turn += 1
        total = len(self.actives) * pow(3, self.dimension)
        count = 0

        actives = set()
        for cube in self.actives:
            count += 1
            print(f'cycle {self.turn}: {count}/{total}', end='\r')
            if self.is_active(cube):
                actives.add(cube)

            for neighbor in self.neighbors(cube):
                count += 1
                print(f'cycle {self.turn}: {count}/{total}', end='\r')
                if self.is_active(neighbor):
                    actives.add(neighbor)
        self.actives = actives
        print(' ' * 50, end='\r')

    def display(self):
        intervals = []
        for i in range(self.dimension):
            coordinates = [coor[i] for coor in self.actives]
            intervals.append(range(min(coordinates), max(coordinates) + 1))

        def layer(z=None, w=None):
            for y in intervals[1]:
                for x in intervals[0]:
                    cube = (x, y)
                    if z != None:
                        cube += (z,)
                    if w != None:
                        cube += (w,)
                    if cube in self.actives:
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')
            print('')

        if self.dimension == 3:
            for z in intervals[2]:
                print(f'z={z}')
                layer(z)
        elif self.dimension == 4:
            for w in intervals[3]:
                for z in intervals[2]:
                    print(f'z={z}, w={w}')
                    layer(z, w)


class Day17:
    def __init__(self, inputs):
        self.initial = {}
        lines = inputs.split('\n')
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                self.initial[(x, y)] = line[x]

    def part1(self):
        pocket = PocketDimension(self.initial, 3)
        for _ in range(6):
            pocket.cycle()
        return len(pocket.actives)

    def part2(self):
        pocket = PocketDimension(self.initial, 4)
        for _ in range(6):
            pocket.cycle()
        return len(pocket.actives)


def main():
    inputs = open("day17.txt").read().strip()
    day17 = Day17(inputs)
    print(f'Part 1: {day17.part1()}')
    print(f'Part 2: {day17.part2()}')


if __name__ == "__main__":
    main()
