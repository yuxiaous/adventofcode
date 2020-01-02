#!/usr/bin/env python3

import math

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        ang = math.atan2(dx, -dy)
        if ang < 0:
            ang += 2 * math.pi
        return ang

    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)

class Day10:
    def __init__(self, data):
        self.asteroids = []

        rows = data.split('\n')
        for y in range(len(rows)):
            row = rows[y]
            for x in range(len(row)):
                area = row[x]
                if area == '#':
                    self.asteroids.append(Asteroid(x, y))

    def detect_from_asteroid(self, asteroid):
        angles = {}
        for other in self.asteroids:
            if other != asteroid:
                angle = asteroid.angle(other)
                if angle not in angles:
                    angles[angle] = []
                angles[angle].append(other)
        # sort
        for angle in angles:
            angles[angle].sort(key=lambda o: asteroid.distance(o))

        return angles

    def part1(self):
        detected = []
        for asteroid in self.asteroids:
            radians = self.detect_from_asteroid(asteroid)
            detected.append((len(radians), asteroid))
        return max(detected)

    def part2(self, best):
        angles = self.detect_from_asteroid(best)
        
        keys = list(angles.keys())
        keys.sort()

        # vaporize asteroids
        vaporized = []
        while True:
            rotate = False
            for key in keys:
                if len(angles[key]) > 0:
                    asteroid = angles[key].pop(0)
                    vaporized.append(asteroid)
                    rotate = True
            if not rotate:
                break

        the200th = vaporized[199]
        return the200th.x * 100 + the200th.y

def main():
    data = open('day10.txt').read().strip()
    day10 = Day10(data)
    num, best = day10.part1()
    xy = day10.part2(best)
    print(f'Part 1: {num}')
    print(f'Part 2: {xy}')

if __name__ == "__main__":
    main()
