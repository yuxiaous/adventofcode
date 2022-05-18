#!/usr/bin/env python3

input = open('day10.txt').read().strip().split('\n')


def part1(input):
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in input:
        stack = []
        for c in line:
            if c in ('(', '[', '{', '<'):
                stack.append(c)
            elif c in (')', ']', '}', '>'):
                o = stack.pop()
                if o + c not in ('()', '[]', '{}', '<>'):
                    # corrupted
                    score += score_map[c]
                    break
    return score


def part2(input):
    score_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in input:
        corrupted = False
        stack = []
        for c in line:
            if c in ('(', '[', '{', '<'):
                stack.append(c)
            elif c in (')', ']', '}', '>'):
                o = stack.pop()
                if o + c not in ('()', '[]', '{}', '<>'):
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                score *= 5
                score += score_map[c]
            scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]


if __name__ == '__main__':
    print('--- Day 10: Syntax Scoring ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
