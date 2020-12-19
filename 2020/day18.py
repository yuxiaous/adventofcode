#!/usr/bin/env python3


class Expression:
    def __init__(self, text):
        self.text = text.replace(' ', '')

    def evaluate1(self):
        def _evaluate(text):
            numbers = []
            operators = []
            i = 0
            while i < len(text):
                c = text[i]
                if c in '+*':
                    operators.append(c)
                    i += 1
                if c.isnumeric():
                    number, length = self.number(text[i:])
                    numbers.append(number)
                    i += length
                elif c == '(':
                    parentheses, length = self.parentheses(text[i:])
                    number = _evaluate(parentheses[1:-1])
                    numbers.append(number)
                    i += length

            result = numbers[0]
            for i in range(len(operators)):
                op = operators[i]
                result = self.operator(op, result, numbers[i+1])
            return result

        return _evaluate(self.text)

    def evaluate2(self):
        def _evaluate(text):
            numbers = []
            operators = []
            i = 0
            while i < len(text):
                c = text[i]
                if c in '+*':
                    operators.append(c)
                    i += 1
                if c.isnumeric():
                    number, length = self.number(text[i:])
                    numbers.append(number)
                    i += length
                elif c == '(':
                    parentheses, length = self.parentheses(text[i:])
                    number = _evaluate(parentheses[1:-1])
                    numbers.append(number)
                    i += length

            while len(numbers) > 1:
                if '+' in operators:
                    i = operators.index('+')
                elif '*' in operators:
                    i = operators.index('*')
                result = self.operator(operators[i], numbers[i], numbers[i+1])
                del operators[i]
                del numbers[i]
                del numbers[i]
                numbers.insert(i, result)
            return numbers[0]

        return _evaluate(self.text)

    def operator(self, op, a, b):
        if op == '+':
            return a + b
        if op == '*':
            return a * b

    def parentheses(self, text):
        stack = []
        for i, c in enumerate(text):
            if c == "(":
                stack.append(i)
            elif c == ")":
                begin = stack.pop()
                if not stack:
                    end = i + 1
                    return text[begin:end], end - begin

    def number(self, text):
        for i, c in enumerate(text):
            if not c.isnumeric():
                return int(text[:i]), i
        return int(text), len(text)


class Day18:
    def __init__(self, inputs):
        self.expressions = [Expression(x) for x in inputs.split('\n')]

    def part1(self):
        results = [exp.evaluate1() for exp in self.expressions]
        return sum(results)

    def part2(self):
        results = [exp.evaluate2() for exp in self.expressions]
        return sum(results)


def main():
    inputs = open("day18.txt").read().strip()
    day18 = Day18(inputs)
    print(f'Part 1: {day18.part1()}')
    print(f'Part 2: {day18.part2()}')


if __name__ == "__main__":
    main()
