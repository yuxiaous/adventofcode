#!/usr/bin/env python3

import re
import math

# test1 = '<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>'
# test2 = '<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>'

class Moon:
    def __init__(self, position):
        reg = r'<x=(\-?\d+),\s*y=(\-?\d+),\s*z=(\-?\d+)>'
        match = re.match(reg, position)
        self.pos = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        self.vel = (0, 0, 0)

    def apply_gravity(self, others):
        vel_x, vel_y, vel_z = self.vel
        for moon in others:
            if moon == self:
                continue
            if moon.pos[0] > self.pos[0]:
                vel_x += 1
            elif moon.pos[0] < self.pos[0]:
                vel_x -= 1
            if moon.pos[1] > self.pos[1]:
                vel_y += 1
            elif moon.pos[1] < self.pos[1]:
                vel_y -= 1
            if moon.pos[2] > self.pos[2]:
                vel_z += 1
            elif moon.pos[2] < self.pos[2]:
                vel_z -= 1
        self.vel = (vel_x, vel_y, vel_z)

    def apply_velocity(self):
        pos_x, pos_y, pos_z = self.pos
        pos_x += self.vel[0]
        pos_y += self.vel[1]
        pos_z += self.vel[2]
        self.pos = (pos_x, pos_y, pos_z)
        
    def energy(self):
        pot = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        kin = abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])
        total = pot * kin
        return total

class Day12:
    def __init__(self, positions):
        self.moons = [Moon(pos) for pos in positions.split('\n')]
        
    def steps(self, n):
        for _ in range(n):
            for moon in self.moons:
                moon.apply_gravity(self.moons)
            for moon in self.moons:
                moon.apply_velocity()

    def energy(self):
        total = 0
        for moon in self.moons:
            total += moon.energy()
        return total

    def part1(self):
        self.steps(1000)
        return self.energy()

    def return_steps(self, axis):
        pos1 = list(map(lambda moon: moon.pos[axis], self.moons))
        vel1 = list(map(lambda moon: moon.vel[axis], self.moons))
        count = 0
        while True:
            count += 1
            self.steps(1)
            pos2 = list(map(lambda moon: moon.pos[axis], self.moons))
            vel2 = list(map(lambda moon: moon.vel[axis], self.moons))
            if pos1 == pos2 and vel1 == vel2:
                return count

    def part2(self):
        return_x = self.return_steps(0)
        return_y = self.return_steps(1)
        return_z = self.return_steps(2)

        # Calculate the least common multiple
        steps = [return_x, return_y, return_z]
        lcm = steps[0]
        for step in steps[1:]:
            lcm = int(lcm*step/math.gcd(lcm, step))
        return lcm

def main():
    positions = open('day12.txt').read().strip()
    day12 = Day12(positions)
    print(f'Part 1: {day12.part1()}')
    print(f'Part 2: {day12.part2()}')

if __name__ == "__main__":
    main()
