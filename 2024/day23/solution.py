import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    connections = set(tuple(sorted(conn.split("-"))) for conn in input.split("\n"))
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

    computers3 = set()
    for c1 in connections.keys():
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


def part2():
    computers_2 = input()

    computers_n = computers_2.copy()
    while True:
        connections: dict[str, set] = {}
        for sets in computers_n:
            for one in sets:
                others = ",".join(sorted(filter(lambda c: c != one, sets)))
                if others not in connections:
                    connections[others] = set()
                connections[others].add(one)

        computers_n = set()
        for c0, neighbors in connections.items():
            for c1 in neighbors:
                for c2 in neighbors:
                    if c1 != c2 and tuple(sorted([c1, c2])) in computers_2:
                        sets = set()
                        sets.update(c0.split(","))
                        sets.add(c1)
                        sets.add(c2)
                        sets = tuple(sorted(list(sets)))
                        computers_n.add(sets)

        print(f"{len(computers_n)}       ", end="\r")
        if len(computers_n) <= 1:
            print(",".join(computers_n.pop()))
            break


part2()
