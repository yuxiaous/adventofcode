#!/usr/bin/env python3
import networkx as nx

input = open('day23.txt').read().strip()
# input = '''#############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########'''
input = input.split('\n')


def parse_input(input, version=1):
    def add_position(pos, sth):
        if sth != '.':
            positions_map[pos] = sth

    positions_map = {}
    add_position('H0', input[1][1])
    add_position('H1', input[1][2])
    add_position('H2', input[1][4])
    add_position('H3', input[1][6])
    add_position('H4', input[1][8])
    add_position('H5', input[1][10])
    add_position('H6', input[1][11])
    if version == 1:
        add_position('A0', input[3][3])
        add_position('A1', input[2][3])
        add_position('B0', input[3][5])
        add_position('B1', input[2][5])
        add_position('C0', input[3][7])
        add_position('C1', input[2][7])
        add_position('D0', input[3][9])
        add_position('D1', input[2][9])
    elif version == 2:
        add_position('A0', input[5][3])
        add_position('A1', input[4][3])
        add_position('A2', input[3][3])
        add_position('A3', input[2][3])
        add_position('B0', input[5][5])
        add_position('B1', input[4][5])
        add_position('B2', input[3][5])
        add_position('B3', input[2][5])
        add_position('C0', input[5][7])
        add_position('C1', input[4][7])
        add_position('C2', input[3][7])
        add_position('C3', input[2][7])
        add_position('D0', input[5][9])
        add_position('D1', input[4][9])
        add_position('D2', input[3][9])
        add_position('D3', input[2][9])

    return positions_map


class Amphipod:
    def __init__(self, type):
        self.type = type
        self.position = None


class Burrow:
    def __init__(self, hallway_size, sideroom_size):
        self.hallway = [f'H{i}' for i in range(hallway_size)]
        self.siderooms = {
            'A': [f'A{i}' for i in range(sideroom_size)],
            'B': [f'B{i}' for i in range(sideroom_size)],
            'C': [f'C{i}' for i in range(sideroom_size)],
            'D': [f'D{i}' for i in range(sideroom_size)],
        }


def get_positions_hash(positions_map, version=1):
    hallway_size = 7
    room_size = [2, 4][version-1]
    hash = []
    for i in range(hallway_size):
        pos = f'H{i}'
        hash.append(positions_map[pos] if pos in positions_map else None)
    for i in 'ABCD':
        for j in range(room_size):
            pos = f'{i}{j}'
            hash.append(positions_map[pos] if pos in positions_map else None)
    return tuple(hash)


def get_positions_map(positions_hash, version=1):
    hallway_size = 7
    room_size = [2, 4][version-1]
    room_num = 4
    positions = {}
    for s in range(hallway_size):
        if positions_hash[s]:
            positions[f'H{s}'] = positions_hash[s]
    for n in range(room_num):
        for s in range(room_size):
            index = 7 + n * room_size + s
            if positions_hash[index]:
                positions[f'{"ABCD"[n]}{s}'] = positions_hash[index]
    return positions


def get_destinations(amphipod: Amphipod, locations, network, burrow: Burrow):
    if amphipod.position in burrow.hallway:
        for pos in burrow.siderooms[amphipod.type]:
            if pos in locations and locations[pos].type != amphipod.type:
                return {}
    else:
        if amphipod.position in burrow.siderooms[amphipod.type]:
            for pos in burrow.siderooms[amphipod.type]:
                if pos == amphipod.position:
                    return {}
                if pos not in locations:
                    break
                if locations[pos].type != amphipod.type:
                    break

    destinations = {}
    paths = nx.shortest_path(
        network, amphipod.position, weight='weight')
    lengths = nx.shortest_path_length(
        network, amphipod.position, weight='weight')
    for dest, path in paths.items():
        if amphipod.position in burrow.hallway:
            if dest in burrow.siderooms[amphipod.type]:
                for pos in burrow.siderooms[amphipod.type]:
                    if pos == dest:
                        destinations[dest] = lengths[dest]
                        break
                    if pos not in locations:
                        break
        elif dest in burrow.hallway:
            destinations[dest] = lengths[dest]
    return destinations


def find_least_energy_organization(configuration, burrow, network: nx.Graph, goal_hash, version=1):
    organizations = {
        get_positions_hash(configuration, version): 0
    }

    while not (len(organizations) == 1 and (goal_hash in organizations)):
        new_organizations = {}
        for organization, energy in organizations.items():
            locations = {}
            amphipods = []
            for pos, type in get_positions_map(organization, version).items():
                amphipod = Amphipod(type)
                amphipod.position = pos
                amphipods.append(amphipod)
                locations[pos] = amphipod

            for amp in amphipods:
                copy = network.copy()
                for pos in locations:
                    if pos != amp.position:
                        copy.remove_node(pos)

                dests = get_destinations(amp, locations, copy, burrow)
                for dest, length in dests.items():
                    positions_map = {p: a.type for p, a in locations.items()}
                    positions_map[dest] = amp.type
                    del positions_map[amp.position]

                    hash = get_positions_hash(positions_map, version)
                    cost = energy + length * {
                        'A': 1, 'B': 10, 'C': 100, 'D': 1000
                    }[amp.type]
                    if hash in new_organizations:
                        if cost < new_organizations[hash]:
                            new_organizations[hash] = cost
                    else:
                        new_organizations[hash] = cost

        organizations = new_organizations
        print('                ', end='\r')
        print(len(organizations), end='\r')

    return organizations[goal_hash]


def part1(input):
    configuration = parse_input(input)

    burrow = Burrow(7, 2)

    network = nx.Graph()
    network.add_edge('H0', 'H1', weight=1)
    network.add_edge('H1', 'H2', weight=2)
    network.add_edge('H2', 'H3', weight=2)
    network.add_edge('H3', 'H4', weight=2)
    network.add_edge('H4', 'H5', weight=2)
    network.add_edge('H5', 'H6', weight=1)
    network.add_edge('A0', 'A1', weight=1)
    network.add_edge('A1', 'H1', weight=2)
    network.add_edge('A1', 'H2', weight=2)
    network.add_edge('B0', 'B1', weight=1)
    network.add_edge('B1', 'H2', weight=2)
    network.add_edge('B1', 'H3', weight=2)
    network.add_edge('C0', 'C1', weight=1)
    network.add_edge('C1', 'H3', weight=2)
    network.add_edge('C1', 'H4', weight=2)
    network.add_edge('D0', 'D1', weight=1)
    network.add_edge('D1', 'H4', weight=2)
    network.add_edge('D1', 'H5', weight=2)

    goal = (None, None, None, None, None, None, None,
            'A', 'A',
            'B', 'B',
            'C', 'C',
            'D', 'D')

    return find_least_energy_organization(configuration, burrow, network, goal)


def part2(input: list[str]):
    input.insert(3, '  #D#C#B#A#  ')
    input.insert(4, '  #D#B#A#C#  ')
    configuration = parse_input(input, version=2)

    burrow = Burrow(7, 4)

    network = nx.Graph()
    network.add_edge('H0', 'H1', weight=1)
    network.add_edge('H1', 'H2', weight=2)
    network.add_edge('H2', 'H3', weight=2)
    network.add_edge('H3', 'H4', weight=2)
    network.add_edge('H4', 'H5', weight=2)
    network.add_edge('H5', 'H6', weight=1)
    network.add_edge('A0', 'A1', weight=1)
    network.add_edge('A1', 'A2', weight=1)
    network.add_edge('A2', 'A3', weight=1)
    network.add_edge('A3', 'H1', weight=2)
    network.add_edge('A3', 'H2', weight=2)
    network.add_edge('B0', 'B1', weight=1)
    network.add_edge('B1', 'B2', weight=1)
    network.add_edge('B2', 'B3', weight=1)
    network.add_edge('B3', 'H2', weight=2)
    network.add_edge('B3', 'H3', weight=2)
    network.add_edge('C0', 'C1', weight=1)
    network.add_edge('C1', 'C2', weight=1)
    network.add_edge('C2', 'C3', weight=1)
    network.add_edge('C3', 'H3', weight=2)
    network.add_edge('C3', 'H4', weight=2)
    network.add_edge('D0', 'D1', weight=1)
    network.add_edge('D1', 'D2', weight=1)
    network.add_edge('D2', 'D3', weight=1)
    network.add_edge('D3', 'H4', weight=2)
    network.add_edge('D3', 'H5', weight=2)

    goal = (None, None, None, None, None, None, None,
            'A', 'A', 'A', 'A',
            'B', 'B', 'B', 'B',
            'C', 'C', 'C', 'C',
            'D', 'D', 'D', 'D')

    return find_least_energy_organization(configuration, burrow, network, goal, version=2)


if __name__ == '__main__':
    print('--- Day 23: Amphipod ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
