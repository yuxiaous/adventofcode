import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    connections = [set(conn.split("-")) for conn in input.split("\n")]
    return connections


def part1():
    computers2 = input()

    connections = {}
    for c1, c2 in computers2:
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()
        connections[c1].add(c2)
        connections[c2].add(c1)

    computers = set()
    for c1, c2 in computers2:
        computers.add(c1)
        computers.add(c2)

    computers3 = set()
    for c1 in computers:
        for c2 in connections[c1]:
            for c3 in connections[c2]:
                if c3 in connections[c1]:
                    sets = tuple(sorted([c1, c2, c3]))
                    computers3.add(sets)

    count = 0
    for cs in computers3:
        for c in cs:
            if c[0] == "t":
                count += 1
                break
    print(count)


part1()

# kh {'qp', 'ub', 'ta', 'tc'}
# tc {'wh', 'kh', 'td', 'co'}
# qp {'wh', 'kh', 'td', 'ub'}
# cg {'yn', 'de', 'aq', 'tb'}
# de {'cg', 'ta', 'co', 'ka'}
# ka {'de', 'ta', 'co', 'tb'}
# co {'ka', 'de', 'ta', 'tc'}
# yn {'wh', 'cg', 'td', 'aq'}
# aq {'yn', 'cg', 'wq', 'vc'}
# ub {'qp', 'kh', 'wq', 'vc'}
# tb {'wq', 'cg', 'ka', 'vc'}
# vc {'ub', 'wq', 'aq', 'tb'}
# wh {'yn', 'qp', 'td', 'tc'}
# ta {'ka', 'kh', 'de', 'co'}
# td {'yn', 'wh', 'qp', 'tc'}
# wq {'aq', 'vc', 'ub', 'tb'}
