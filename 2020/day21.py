#!/usr/bin/env python3

import re


class Food:
    def __init__(self, info):
        m = re.match(r'(.+) \(contains (.+)\)', info)
        self.ingredients = m.group(1).split(' ')
        self.allergens = m.group(2).split(', ')


class Day21:
    def __init__(self, inputs):
        self.foods = [Food(x) for x in inputs.split('\n')]
        self.ingredients = set()
        self.allergens = set()
        self.counter = {}

        for food in self.foods:
            for ingredient in food.ingredients:
                self.ingredients.add(ingredient)
                for allergen in food.allergens:
                    self.allergens.add(allergen)

                    key = (ingredient, allergen)
                    if key not in self.counter:
                        self.counter[key] = 0
                    self.counter[key] += 1

    def part1(self):
        for allergen in self.allergens:
            keys = [(ingr, alle)
                    for ingr, alle in self.counter if alle == allergen]
            largest = max(keys, key=lambda k: self.counter[k])
            removes = []
            for ingr, alle in self.counter:
                if alle == allergen:
                    if self.counter[(ingr, alle)] < self.counter[largest]:
                        removes.append((ingr, alle))
            for remove in removes:
                del self.counter[remove]

        possibles = set(ingr for ingr, alle in self.counter)
        inerts = set(
            ingredient for ingredient in self.ingredients if ingredient not in possibles)

        count = 0
        for inert in inerts:
            for food in self.foods:
                if inert in food.ingredients:
                    count += 1
        return count

    def part2(self):
        ingredients = set()
        allergens = set()
        for ingr, alle in self.counter:
            ingredients.add(ingr)
            allergens.add(alle)

        #           dairy   fish    nuts    peanuts     sesame      shellfish   soy     wheat
        # ltbj      13
        # nrfmm             9
        # pvhcsn                    12
        # jxbnb                             6
        # chpdjkf                                       14
        # jtqt                                                      7
        # zzkq                                                                  10
        # jqnhd                                                                         12


def main():
    inputs = open("day21.txt").read().strip()
    day21 = Day21(inputs)
    print(f'Part 1: {day21.part1()}')
    print(f'Part 2: {day21.part2()}')


if __name__ == "__main__":
    main()
