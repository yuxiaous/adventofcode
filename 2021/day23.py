#!/usr/bin/env python3
import networkx as nx

input = open('day23.txt').read().strip()


def parse_input(input: str):
    input = input.split('\n')
    positions = {}

    def add_position(pos, sth):
        if sth != '.':
            positions[pos] = sth

    add_position('H0', input[1][1])
    add_position('H1', input[1][2])
    add_position('H2', input[1][4])
    add_position('H3', input[1][6])
    add_position('H4', input[1][8])
    add_position('H5', input[1][10])
    add_position('H6', input[1][11])
    add_position('A0', input[3][3])
    add_position('A1', input[2][3])
    add_position('B0', input[3][5])
    add_position('B1', input[2][5])
    add_position('C0', input[3][7])
    add_position('C1', input[2][7])
    add_position('D0', input[3][9])
    add_position('D1', input[2][9])
    return positions


class Amphipod:
    def __init__(self, type):
        self.type = type
        self.position = None


def get_destinations(amphipod: Amphipod, positions, diagram):
    if amphipod.position[0] == 'H':
        for i in range(2):
            pos = f'{amphipod.type}{i}'
            if pos in positions and positions[pos].type != amphipod.type:
                return {}, {}
    elif amphipod.position[0] == amphipod.type:
        if amphipod.position[1] == '0':
            return {}, {}
        if amphipod.position[1] == '1':
            pos = f'{amphipod.position[0]}0'
            if pos in positions and positions[pos].type == amphipod.type:
                return {}, {}
    else:
        if amphipod.position[1] == '0':
            pos = f'{amphipod.position[0]}1'
            if pos in positions:
                return {}, {}

    paths: dict = nx.shortest_path(diagram, amphipod.position)
    lengths = nx.shortest_path_length(
        diagram, amphipod.position, weight='weight')
    for dest, path in paths.copy().items():
        if dest == amphipod.position:
            del paths[dest]
            del lengths[dest]
        elif dest[0] != 'H' and dest[0] != amphipod.type:
            del paths[dest]
            del lengths[dest]
        elif dest[0] == 'H' and amphipod.position[0] == 'H':
            del paths[dest]
            del lengths[dest]
        elif dest == f'{amphipod.type}1':
            if f'{amphipod.type}0' not in positions:
                del paths[dest]
                del lengths[dest]
            elif positions[f'{amphipod.type}0'].type != amphipod.type:
                del paths[dest]
                del lengths[dest]
        for pos in positions:
            if pos in path[1:] and dest in paths:
                del paths[dest]
                del lengths[dest]
    return paths, lengths


def get_positions_hash(positions):
    hash = []
    for i in range(7):
        pos = f'H{i}'
        hash.append(positions[pos] if pos in positions else None)
    for i in 'ABCD':
        for j in range(2):
            pos = f'{i}{j}'
            hash.append(positions[pos] if pos in positions else None)
    return tuple(hash)


def get_positions(hash):
    positions = {}
    for i in range(7):
        positions[f'H{i}'] = hash[i]
    for i in range(4):
        for j in range(2):
            positions[f'{"ABCD"[i]}{j}'] = hash[7 + i * 2 + j]
    return positions


def part1(input):
    diagram = nx.Graph()
    diagram.add_edge('H0', 'H1', weight=1)
    diagram.add_edge('H1', 'H2', weight=2)
    diagram.add_edge('H2', 'H3', weight=2)
    diagram.add_edge('H3', 'H4', weight=2)
    diagram.add_edge('H4', 'H5', weight=2)
    diagram.add_edge('H5', 'H6', weight=1)
    diagram.add_edge('A0', 'A1', weight=1)
    diagram.add_edge('A1', 'H1', weight=2)
    diagram.add_edge('A1', 'H2', weight=2)
    diagram.add_edge('B0', 'B1', weight=1)
    diagram.add_edge('B1', 'H2', weight=2)
    diagram.add_edge('B1', 'H3', weight=2)
    diagram.add_edge('C0', 'C1', weight=1)
    diagram.add_edge('C1', 'H3', weight=2)
    diagram.add_edge('C1', 'H4', weight=2)
    diagram.add_edge('D0', 'D1', weight=1)
    diagram.add_edge('D1', 'H4', weight=2)
    diagram.add_edge('D1', 'H5', weight=2)

    positions = parse_input(input)

    organizations = {
        get_positions_hash(positions): 0
    }
    # print(organizations)

    histories = {}

    final = (None, None, None, None, None, None, None,
             'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D')

    while len(organizations) > 1 or (final not in organizations):
        new_organizations = {}
        for organization, energy in organizations.items():
            locations = {}
            amphipods = []
            for p, t in get_positions(organization).items():
                if t:
                    amphipod = Amphipod(t)
                    amphipod.position = p
                    amphipods.append(amphipod)
                    locations[p] = amphipod

            for amp in amphipods:
                paths, lengths = get_destinations(amp, locations, diagram)
                for dest, path in paths.items():
                    positions = {p: a.type for p, a in locations.items()}
                    positions[dest] = amp.type
                    del positions[amp.position]

                    hash = get_positions_hash(positions)
                    cost = energy + lengths[dest] * {'A': 1, 'B': 10,
                                                     'C': 100, 'D': 1000}[amp.type]
                    if hash in new_organizations:
                        if cost < new_organizations[hash]:
                            new_organizations[hash] = cost
                            histories[hash] = organization
                    else:
                        new_organizations[hash] = cost
                        histories[hash] = organization

        organizations = new_organizations
        print(len(organizations))

    hash = final
    while hash in histories:
        print(hash)
        pre = histories[hash]
        hash = pre

    return organizations[final]


def part2(input):
    pass


if __name__ == '__main__':
    print('--- Day 23: Amphipod ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
