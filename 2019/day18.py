#!/usr/bin/env python3

import networkx as nx
from itertools import combinations

test1 = '########################\n#...............b.C.D.f#\n#.######################\n#.....@.a.B.c.d.A.e.F.g#\n########################'
test2 = '#################\n#i.G..c...e..H.p#\n########.########\n#j.A..b...f..D.o#\n########@########\n#k.E..a...g..B.n#\n########.########\n#l.F..d...h..C.m#\n#################'
test3 = '########################\n#@..............ac.GI.b#\n###d#e#f################\n###A#B#C################\n###g#h#i################\n########################'

ENTRANCE = '@'
PASSAGE = '.'
WALL = '#'

def is_key(what):
    return what.islower()

def is_door(what):
    return what.isupper()

def phash(path):
    return tuple(path[:1] + path[-1:] + sorted(path[1:-1]))

class Day18:
    def __init__(self, data):
        self.map = [[c for c in r] for r in data.split('\n')]
        self.events = self._events()
        self.neighbors = {e: self._neighbors(p) for e, p in self.events.items()}
        self.graph = self._graph()

    def _events(self):
        events = {}
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                what = self.map[r][c]
                if what == ENTRANCE:
                    events[what] = (r, c)
                elif is_key(what):
                    events[what] = (r, c)
                elif is_door(what):
                    events[what] = (r, c)
        return events

    def _neighbors(self, start):
        opened = [start]
        closed = []
        neighbors = {}
        step = 0
        while True:
            step += 1
            temp = opened
            opened = []
            for pos in temp:
                closed.append(pos)
                u = (pos[0] - 1, pos[1])
                d = (pos[0] + 1, pos[1])
                l = (pos[0], pos[1] - 1)
                r = (pos[0], pos[1] + 1)
                for direction in (u, d, l, r):
                    if direction in opened:
                        continue
                    if direction in closed:
                        continue
                    what = self.map[direction[0]][direction[1]]
                    if what in (PASSAGE, ENTRANCE):
                        opened.append(direction)
                    elif is_door(what) or is_key(what):
                        neighbors[what] = step
            if not opened:
                return neighbors

    def _graph(self):
        graph = nx.Graph()
        for e1 in self.neighbors:
            for e2 in self.neighbors[e1]:
                length = self.neighbors[e1][e2]
                graph.add_edge(e1, e2, length = length)
        return graph

    def collect(self):
        first = [ENTRANCE]
        opened = {phash(first): (0, first)}
        all_keys = [e for e in self.events if is_key(e)]

        count = 0
        while True:
            print(f'{count}/{len(all_keys)}', end='\r')
            count += 1

            temp = opened
            opened = {}
            for h in temp:
                length, path = temp[h]
                for next_key in all_keys:
                    # if the key was collected
                    if next_key in path:
                        continue
                    # path to new key
                    shortest_path = nx.shortest_path(self.graph, path[-1], next_key, weight = 'length')
                    shortest_len = nx.shortest_path_length(self.graph, path[-1], next_key, weight = 'length')
                    need_keys = [str.lower(x) for x in shortest_path[1:-1]]
                    # if reachable
                    if set(need_keys).issubset(set(path)):
                        new_path = path + [next_key]
                        new_length = length + shortest_len
                        new_hash = phash(new_path)
                        # save best path
                        if new_hash in opened:
                            if new_length < opened[new_hash][0]:
                                opened[new_hash] = (new_length, new_path)
                        else:
                            opened[new_hash] = (new_length, new_path)
            # if all keys were collected
            if not opened:
                return temp[min(temp, key=lambda h: temp[h][0])]

    def part1(self):
        length, path = self.collect()
        print(path)
        return length

    def part2(self):
        pass

def main():
    data = open('day18.txt').read().strip()
    day18 = Day18(data)
    print(f'Part 1: {day18.part1()}')
    print(f'Part 2: {day18.part2()}')

if __name__ == "__main__":
    main()
