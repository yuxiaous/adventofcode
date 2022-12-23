#!/usr/bin/env python3
import re
from functools import reduce

input = open("day11.txt").read().strip()


class Monkey:
    def __init__(self, note: str) -> None:
        match = re.match(
            r"Monkey (\d+):\s+Starting items: (.+)\s+Operation: (.+)\s+Test: divisible by (\d+)\s+If true: throw to monkey (.+)\s+If false: throw to monkey (.+)",
            note,
        )
        if match:
            self.index = int(match.group(1))
            self.items = [int(x) for x in match.group(2).split(", ")]

            def operation(old):
                loc = {}
                exec(f"old={old}; {match.group(3)}", globals(), loc)
                return loc["new"]

            self.operation = operation

            self.divisor = int(match.group(4))

            def test(worry):
                result = worry % self.divisor == 0
                if result:
                    return int(match.group(5))
                else:
                    return int(match.group(6))

            self.test = test

        self.currnet = None
        self.times = 0

    def inspect(self, relieve):
        if len(self.items) > 0:
            self.times += 1
            self.currnet = self.items.pop(0)
            self.currnet = self.operation(self.currnet)
            self.currnet = relieve(self.currnet)
            return True
        return False

    def throw(self):
        index = self.test(self.currnet)
        return index

    def catch(self, item):
        self.items.append(item)


def part1():
    monkeys = [Monkey(n) for n in input.split("\n\n")]

    def relieve(worry: int):
        return int(worry / 3)

    round = 20
    for _ in range(round):
        for monkey in monkeys:
            while monkey.inspect(relieve):
                index = monkey.throw()
                monkeys[index].catch(monkey.currnet)

    times = [m.times for m in monkeys]
    times.sort(reverse=True)
    return times[0] * times[1]


def part2():
    monkeys = [Monkey(n) for n in input.split("\n\n")]

    divisor = reduce((lambda x, y: x * y), [m.divisor for m in monkeys])

    def relieve(worry: int):
        return worry % divisor

    round = 10000
    for r in range(round):
        for monkey in monkeys:
            while monkey.inspect(relieve):
                index = monkey.throw()
                monkeys[index].catch(monkey.currnet)

        print(f"{r+1}/{round}", end="\r")

    times = [m.times for m in monkeys]
    times.sort(reverse=True)
    return times[0] * times[1]


if __name__ == "__main__":
    print("--- Day 11: Monkey in the Middle ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
