#!/usr/bin/env python3

import re

input = open('day21.txt').read().strip()


class Dice:
    def __init__(self, side):
        self.side = side


class DeterministicDice(Dice):
    def __init__(self, side):
        super().__init__(side)
        self.times = 0
        self.current = 0

    def roll(self):
        self.times += 1
        self.current += 1
        while self.current > self.side:
            self.current -= self.side
        return self.current


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class GameBoard:
    def __init__(self, space):
        self.space = space
        self.positions = {}

    def set_player(self, player, position):
        self.positions[player] = position

    def move(self, player: Player, point: int):
        if player in self.positions:
            position = self.positions[player]
            position += point
            while position > self.space:
                position -= self.space
            self.positions[player] = position
        return position


def parse_player(entry):
    match = re.match(r'(Player \d+) starting position: (\d+)', entry)
    name = match.group(1)
    position = int(match.group(2))
    return name, position


def part1(input: str):
    # init
    board = GameBoard(10)
    die = DeterministicDice(100)
    players: list[Player] = []
    for entry in input.split('\n'):
        name, position = parse_player(entry)
        player = Player(name)
        players.append(player)
        board.set_player(player, position)

    def turn(player: Player):
        # roll three times
        point = die.roll() + die.roll() + die.roll()
        # move spaces
        space = board.move(player, point)
        # add score
        player.score += space
        # check if the player wins the game
        return player.score < 1000

    # start game
    current = 0
    while turn(players[current]):
        current += 1
        while current >= len(players):
            current -= len(players)

    return players[current-1].score * die.times


def part2(input: str):
    pass


if __name__ == '__main__':
    print('--- Day 21: Dirac Dice ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
