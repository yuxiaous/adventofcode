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
    return tuple(path[-1:] + sorted(path[:-1]))

def ghash(graph):
    return tuple(sorted(graph.nodes()))

class Day18:
    def __init__(self, data):
        self.map = [[c for c in r] for r in data.split('\n')]
        self.events = {}
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                what = self.map[r][c]
                if is_key(what):
                    self.events[what] = (r, c)
                elif is_door(what):
                    self.events[what] = (r, c)

    def _entrances(self):
        entrances = []
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                what = self.map[r][c]
                if what == ENTRANCE:
                    entrances.append((r, c))
        return entrances

    def _neighbors(self, pos):
        opened = [pos]
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

    def _edges(self, start):
        edges = {}
        edges[ENTRANCE] = self._neighbors(start)

        opened = list(edges[ENTRANCE])
        closed = []
        while True:
            temp = opened
            opened = []
            for e in temp:
                closed.append(e)
                pos = self.events[e]
                edges[e] = self._neighbors(pos)
                for n in edges[e]:
                    if n in opened:
                        continue
                    if n in closed:
                        continue
                    opened.append(n)
            if not opened:
                return edges

    def _graph(self, start):
        edges = self._edges(start)
        graph = nx.Graph()
        for e1 in edges:
            for e2 in edges[e1]:
                length = edges[e1][e2]
                graph.add_edge(e1, e2, length = length)
        return graph

    def collect(self, graphs):
        first = [ENTRANCE]
        lasts = {ghash(graph): ENTRANCE for graph in graphs}
        opened = {phash(first): (0, first, lasts)}
        all_keys = [e for e in self.events if is_key(e)]

        count = 0
        while True:
            print(f'{count}/{len(all_keys)}', end='\r')
            count += 1

            temp = opened
            opened = {}
            for h in temp:
                length, path, lasts = temp[h]
                for next_key in all_keys:
                    # if the key was collected
                    if next_key in path:
                        continue
                    # which graph is the key in
                    for graph in graphs:
                        if next_key in graph:
                            last = lasts[ghash(graph)]
                            # path to new key
                            shortest_path = nx.shortest_path(graph, last, next_key, weight = 'length')
                            shortest_len = nx.shortest_path_length(graph, last, next_key, weight = 'length')
                            need_keys = [str.lower(x) for x in shortest_path[1:-1]]
                            # if reachable
                            if set(need_keys).issubset(set(path)):
                                new_path = path + [next_key]
                                new_length = length + shortest_len
                                new_hash = phash(new_path)
                                new_lasts = lasts.copy()
                                new_lasts[ghash(graph)] = next_key
                                # save best path
                                if new_hash in opened:
                                    if new_length < opened[new_hash][0]:
                                        opened[new_hash] = (new_length, new_path, new_lasts)
                                else:
                                    opened[new_hash] = (new_length, new_path, new_lasts)
            # if all keys were collected
            if not opened:
                return temp[min(temp, key=lambda h: temp[h][0])][:2]

    def part1(self):
        entrances = self._entrances()
        graph = self._graph(entrances[0])
        length, path = self.collect([graph])
        print(path)
        return length

    def part2(self):
        entrances = self._entrances()
        r, c = entrances[0]
        self.map[r-1][c-1:c+2] = list('@#@')
        self.map[r  ][c-1:c+2] = list('###')
        self.map[r+1][c-1:c+2] = list('@#@')

        entrances = self._entrances()
        graphs = [self._graph(entrance) for entrance in entrances]
        length, path = self.collect(graphs)
        print(path)
        return length

def main():
    data = open('day18.txt').read().strip()
    day18 = Day18(data)
    print(f'Part 1: {day18.part1()}')
    print(f'Part 2: {day18.part2()}')

if __name__ == "__main__":
    main()
