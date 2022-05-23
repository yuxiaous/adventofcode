#!/usr/bin/env python3
import re

input = open('day17.txt').read().strip()


def get_position_x(v, n):
    if n < v:
        return int(v * n + n * (1 - n) / 2)
    else:
        return int(v * (1 + v) / 2)


def get_position_y(v, n):
    return n * v - n * (n - 1) / 2


def get_max_target_position_x(initial_velocity_x):
    return initial_velocity_x * (1 + initial_velocity_x) / 2


def get_max_initial_velocity_y(target_position_y):
    if target_position_y > 0:
        return target_position_y
    elif target_position_y < 0:
        return -target_position_y - 1


def part1(input):
    '''只考虑 y 轴方向，令初始速度为 v ，目标位置为 p ，经过的步数为 n。
    第 1 步后， p = v;
    第 2 步后， p = v + (v - 1);
    第 3 步后， p = v + (v - 1) + (v - 2);
    第 n 步后， p = v + (v - 1) + (v - 2) + ... + (v - (n - 1));
    根据等差数列求和公式，得
    第 n 步后， p = n * v - n * (n - 1) / 2。
    经过转换，得到 v = p / n + (n - 1) / 2。
    根据条件： v、p 是整数， n 是正整数，
    - 当 p > 0 时（即目标位置在初始位置上方时），令 n = 2p ，可得整数解 v = p;
    - 当 p < 0 时（即目标位置在初始位置下方时），令 n = -2p ，可的整数解 v = -p - 1;
    - 当 p = 0 时（即目标位置与初始位置相同时），初始速度 v 与 目标位置 p 无关。
    '''

    m = re.match('target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)', input)
    min_target_position_y = int(m.group(3))
    max_target_position_y = int(m.group(4))

    initial_velocity_y = max(
        get_max_initial_velocity_y(min_target_position_y),
        get_max_initial_velocity_y(max_target_position_y))

    if initial_velocity_y > 0:
        step = 0
        max_position_y = 0
        while True:
            step += 1
            py = get_position_y(initial_velocity_y, step)
            if py > max_position_y:
                max_position_y = py
            elif py < max_position_y:
                return int(max_position_y)


def part2(input):
    m = re.match('target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)', input)
    min_target_position_x = int(m.group(1))
    max_target_position_x = int(m.group(2))
    min_target_position_y = int(m.group(3))
    max_target_position_y = int(m.group(4))

    # find initial y velocity range
    min_initial_velocity_y = min(min_target_position_y, max_target_position_y)
    max_initial_velocity_y = max(
        get_max_initial_velocity_y(min_target_position_y),
        get_max_initial_velocity_y(max_target_position_y))

    # find initial x velocity range
    max_initial_velocity_x = max(min_target_position_x, max_target_position_x)
    min_initial_velocity_x = 0
    while True:
        min_initial_velocity_x += 1
        px = get_max_target_position_x(min_initial_velocity_x)
        if px >= min_target_position_x:
            break

    # find max number of step
    max_step = 0
    while True:
        max_step += 1
        py = get_position_y(max_initial_velocity_y, max_step)
        if py == min_target_position_y:
            break

    initial_velocity = set()
    for n in range(max_step + 1):
        for vx in range(min_initial_velocity_x, max_initial_velocity_x + 1):
            for vy in range(min_initial_velocity_y, max_initial_velocity_y + 1):
                px = get_position_x(vx, n)
                py = get_position_y(vy, n)
                if (min_target_position_x <= px <= max_target_position_x
                        and min_target_position_y <= py <= max_target_position_y):
                    initial_velocity.add((vx, vy))
    return len(initial_velocity)


if __name__ == '__main__':
    print('--- Day 17: Trick Shot ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
