#!/usr/bin/env python3

import re


class Day19:
    def __init__(self, inputs):
        inputs = inputs.split('\n\n')
        self.rules = {}
        for rule in inputs[0].split('\n'):
            m = re.match(r'(\d+): (.+)', rule)
            key = int(m.group(1))
            subrules = m.group(2)

            def parse(subrule):
                if '"' in subrule:
                    return re.match(r'\"(\w+)\"', subrule).group(1)
                else:
                    return tuple(int(x) for x in re.findall(r'(\d+)', subrule))

            if '|' in subrules:
                self.rules[key] = []
                for subrule in subrules.split('|'):
                    self.rules[key].append(parse(subrule))
            else:
                self.rules[key] = [parse(subrules)]

        self.messages = [x for x in inputs[1].split('\n')]

    def part1(self):

        def multiply(message):
            result = [()]
            for i in range(len(message)):
                result = [x + y if isinstance(y, tuple) else x + (y,)
                          for x in result for y in message[i]]
            return result

        def rules(id):
            messages = []
            for message in self.rules[id]:
                if isinstance(message, str):
                    messages.append(message)
                else:
                    a = tuple(rules(x) for x in message)
                    messages.extend(multiply(a))
            return messages

        matches = [''.join(message) for message in rules(0)]

        count = 0
        length = len(self.messages)
        for i in range(len(self.messages)):
            print(f'{i}/{length}', end='\r')
            message = self.messages[i]
            if message in matches:
                count += 1
        return count

    def part2(self):
        pass


def main():
    inputs = open("day19.txt").read().strip()
    day19 = Day19(inputs)
    print(f'Part 1: {day19.part1()}')
    print(f'Part 2: {day19.part2()}')


if __name__ == "__main__":
    main()
