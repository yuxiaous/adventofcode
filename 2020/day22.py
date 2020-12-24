#!/usr/bin/env python3

import re


class Player:
    def __init__(self, index, cards):
        self.index = index
        self.cards = cards
        self.saves = set()

    def draw(self):
        return self.cards.pop(0)

    def keep(self, cards):
        self.cards.append(cards.pop(self.index))
        self.cards.extend(cards)

    def save(self):
        uuid = hash(tuple(self.cards))
        if uuid not in self.saves:
            self.saves.add(uuid)
            return True
        return False


class CombatGame:
    def __init__(self, decks):
        self.players = [Player(i, decks[i][:]) for i in range(len(decks))]
        self.count = 0
        self.end = False
        self.winner = None

    def round(self):
        self.count += 1
        print(self.count, end='\r')

        draws = []
        for player in self.players:
            card = player.draw()
            draws.append(card)

        higher = draws.index(max(draws))
        winner = self.players[higher]

        winner.keep(draws)

        self.end = any([len(player.cards) == 0 for player in self.players])
        if self.end:
            self.winner = winner

    def play(self):
        while not self.end:
            self.round()


class RecursiveCombatGame:
    index = 0

    def __init__(self, decks):
        RecursiveCombatGame.index += 1
        print(RecursiveCombatGame.index, end='\r')

        self.players = [Player(i, decks[i][:]) for i in range(len(decks))]
        self.count = 0
        self.end = False
        self.winner = None
        self.index = RecursiveCombatGame.index

    def round(self):
        self.count += 1

        for player in self.players:
            if not player.save():
                self.end = True
                self.winner = self.players[0]
                return

        draws = []
        for player in self.players:
            card = player.draw()
            draws.append(card)

        if all([len(self.players[i].cards) >= draws[i] for i in range(len(self.players))]):
            subgame = RecursiveCombatGame(
                [self.players[i].cards[:draws[i]] for i in range(len(self.players))])
            while not subgame.end:
                subgame.round()
            winner = self.players[subgame.winner.index]
        else:
            higher = draws.index(max(draws))
            winner = self.players[higher]

        winner.keep(draws)

        self.end = any([len(player.cards) == 0 for player in self.players])
        if self.end:
            self.winner = winner

    def play(self):
        while not self.end:
            self.round()


class Day22:
    def __init__(self, inputs):
        self.decks = []
        for data in inputs.split('\n\n'):
            m = re.match(r'Player \d:\n([\d\n]+)', data)
            cards = [int(x) for x in m.group(1).split('\n')]
            self.decks.append(cards)

    def score(self, game):
        score = 0
        length = len(game.winner.cards)
        for i in range(length):
            card = game.winner.cards[i]
            score += card * (length - i)
        return score

    def part1(self):
        game = CombatGame(self.decks)
        game.play()
        return self.score(game)

    def part2(self):
        game = RecursiveCombatGame(self.decks)
        game.play()
        return self.score(game)


def main():
    inputs = open("day22.txt").read().strip()
    day22 = Day22(inputs)
    print(f'Part 1: {day22.part1()}')
    print(f'Part 2: {day22.part2()}')


if __name__ == "__main__":
    main()
