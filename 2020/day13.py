#!/usr/bin/env python3


class Day13:
    def __init__(self, inputs):
        notes = inputs.split('\n')
        self.earliest = int(notes[0])
        self.schedule = notes[1].split(',')

    def part1(self):
        ids = [int(id) for id in self.schedule if id != 'x']
        waits = [id - self.earliest % id for id in ids]
        wait = min(waits)
        index = waits.index(wait)
        id = ids[index]
        return id * wait

    def part2(self):
        contest = {}
        for i in range(len(self.schedule)):
            id = self.schedule[i]
            if id != 'x':
                contest[i] = int(id)

        last = (0, 1)
        for offset in contest:
            interval = contest[offset]

            times = 1
            earliest = None
            while True:
                t = last[0] + last[1] * times
                print(t, end='\r')
                if (t + offset) % interval == 0:
                    if earliest == None:
                        earliest = t
                    else:
                        last = (earliest, t - earliest)
                        break
                times += 1

        return earliest


def main():
    inputs = open("day13.txt").read().strip()
    day13 = Day13(inputs)
    print(f'Part 1: {day13.part1()}')
    print(f'Part 2: {day13.part2()}')


if __name__ == "__main__":
    main()
