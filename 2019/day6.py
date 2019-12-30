#!/usr/bin/env python3

# test1 = 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'
# test2 = 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN'

class Day6:
    def __init__(self, input):
        self.orbits = {}

        for orbit in input.split('\n'):
            parent, child = orbit.split(')')
            self.orbits[child] = parent

    def get_orbits_chain(self, obj):
        chain = []
        while obj in self.orbits:
            parent = self.orbits[obj]
            chain.append(parent)
            obj = parent
        chain.reverse()
        return chain

    def part1(self):
        total = 0
        for obj in self.orbits:
            chain = self.get_orbits_chain(obj)
            total += len(chain)
        return total

    def part2(self):
        chain_you = self.get_orbits_chain('YOU')
        chain_san = self.get_orbits_chain('SAN')

        while chain_you[0] == chain_san[0]:
            chain_you.pop(0)
            chain_san.pop(0)

        return len(chain_you) + len(chain_san)

def main():
    input = open('day6.txt').read().strip()
    # input = test2
    day6 = Day6(input)
    print(f'Part 1: {day6.part1()}')
    print(f'Part 2: {day6.part2()}')

if __name__ == "__main__":
    main()
