#!/usr/bin/env python3

input = [x for x in open("day02.txt").read().strip().split("\n")]
guide = [x.split() for x in input]


win_map = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
}

lose_map = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}


def play(op, me) -> int:
    shape_score = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }
    outcome_score = {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    if me == win_map[op]:
        outcome = "win"
    elif me == lose_map[op]:
        outcome = "lose"
    else:
        outcome = "draw"

    return shape_score[me] + outcome_score[outcome]


def part1():
    guide_map = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    total = 0
    for round in guide:
        op = guide_map[round[0]]
        me = guide_map[round[1]]
        score = play(op, me)
        total += score

    return total


def part2():
    guide_map = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    total = 0
    for round in guide:
        op = guide_map[round[0]]

        if guide_map[round[1]] == "lose":
            me = lose_map[op]
        elif guide_map[round[1]] == "win":
            me = win_map[op]
        else:
            me = op

        score = play(op, me)
        total += score

    return total


if __name__ == "__main__":
    print("--- Day 2: Rock Paper Scissors ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
