#!/usr/bin/env python3

from computer import ASCII

class Camera:
    def __init__(self, codes):
        self.computer = ASCII(codes)
        self.image = []

    def take_image(self):
        while True:
            status = self.computer.run()
            if status == ASCII.OUTPUT:
                line = self.computer.output()[:-1]
                if line:
                    self.image.append([c for c in line])
            elif status == ASCII.HALT:
                break

    def calibrate(self):
        apsum = 0
        for r in range(1, len(self.image) - 1):
            for c in range(1, len(self.image[r]) - 1):
                if self.image[r][c] != '#':
                    continue
                if self.image[r - 1][c] != '#':
                    continue
                if self.image[r + 1][c] != '#':
                    continue
                if self.image[r][c - 1] != '#':
                    continue
                if self.image[r][c + 1] != '#':
                    continue
                self.image[r][c] = 'O'
                apsum += r * c
        return apsum

    def draw(self):
        for line in self.image:
            print(''.join(line))

class VacuumRobot:
    def __init__(self, codes):
        self.computer = ASCII(codes)

    def wake_up(self, rules):
        self.computer.memory[0] = 2
        while True:
            status = self.computer.run()
            if status == ASCII.INPUT:
                if len(rules) > 0:
                    rule = rules.pop(0)
                    print(rule)
                else:
                    rule = input()
                self.computer.input(rule)
            elif status == ASCII.OUTPUT:
                code = self.computer.output()
                if isinstance(code, str):
                    print(code, end='')
                else:
                    return code
            elif status == ASCII.HALT:
                break

class Day17:
    def __init__(self, program):
        self.codes = [int(x) for x in program.split(',')]

    def part1(self):
        camera = Camera(self.codes)
        camera.take_image()
        ret = camera.calibrate()
        camera.draw()
        return ret

    # R,8,L,12,R,8,R,8,L,12,R,8,L,10,L,10,R,8,L,12,L,12,L,10,R,10,L,10,L,10,R,8,L,12,L,12,L,10,R,10,L,10,L,10,R,8,R,8,L,12,R,8,L,12,L,12,L,10,R,10,R,8,L,12,R,8
    def part2(self):
        robot = VacuumRobot(self.codes)
        return robot.wake_up([
            'A,A,B,C,B,C,B,A,C,A',
            'R,8,L,12,R,8',
            'L,10,L,10,R,8',
            'L,12,L,12,L,10,R,10',
            'n'
        ])

def main():
    program = open('day17.txt').read().strip()
    day17 = Day17(program)
    print(f'Part 1: {day17.part1()}')
    print(f'Part 2: {day17.part2()}')

if __name__ == "__main__":
    main()
