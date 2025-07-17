import os

os.chdir(os.path.dirname(__file__))


def input(wide=False):
    input = open("input.txt").read().strip()
    document = input.split("\n\n")
    map = [[x for x in l] for l in document[0].split("\n")]
    moves = [x for x in document[1] if x != "\n"]

    if wide:
        twice = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        for i in range(len(map)):
            line = map[i]
            newline = []
            for tile in line:
                newline += twice[tile]
            map[i] = newline

    return map, moves


def print_map(map):
    h, w = len(map), len(map[0])
    for y in range(h):
        for x in range(w):
            print(map[y][x], end="")
        print("")
    print("")


def find_robot(map):
    h, w = len(map), len(map[0])
    for y in range(h):
        for x in range(w):
            if map[y][x] == "@":
                return (x, y)


def part1():
    map, moves = input()
    h, w = len(map), len(map[0])
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    # print("Initial state:")
    # print_map(map)

    robot = find_robot(map)
    for m in moves:
        dx, dy = directions[m]
        x = robot[0] + dx
        y = robot[1] + dy
        while x in range(w) or y in range(h):
            if map[y][x] == "#":
                break
            elif map[y][x] == "O":
                x += dx
                y += dy
            elif map[y][x] == ".":
                while map[y][x] != "@":
                    map[y][x] = map[y - dy][x - dx]
                    x -= dx
                    y -= dy
                map[y][x] = "."
                robot = (x + dx, y + dy)
                break

        # print(f"Move {m}:")
        # print_map(map)

    gps = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == "O":
                gps += y * 100 + x
    print(gps)


part1()


def part2():
    map, moves = input(True)
    h, w = len(map), len(map[0])
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    def test(position, direction):
        dx, dy = direction
        x = position[0] + dx
        y = position[1] + dy

        if map[y][x] == "#":
            return False
        elif map[y][x] == ".":
            return True
        elif map[y][x] == "[":
            if dx == 0:
                return test((x, y), direction) and test((x + 1, y), direction)
            else:
                return test((x + 1, y), direction)
        elif map[y][x] == "]":
            if dx == 0:
                return test((x, y), direction) and test((x - 1, y), direction)
            else:
                return test((x - 1, y), direction)
        return False

    def push(position, direction):
        dx, dy = direction
        x = position[0] + dx
        y = position[1] + dy

        if map[y][x] == "#":
            return position
        elif map[y][x] == ".":
            pass
        elif map[y][x] == "[":
            push((x, y), direction)
            if dx == 0:
                push((x + 1, y), direction)
        elif map[y][x] == "]":
            push((x, y), direction)
            if dx == 0:
                push((x - 1, y), direction)

        map[y][x] = map[y - dy][x - dx]
        map[y - dy][x - dx] = "."
        return (x, y)

    # print("Initial state:")
    # print_map(map)

    robot = find_robot(map)
    for m in moves:
        if test(robot, directions[m]):
            robot = push(robot, directions[m])

        # print(f"Move {m}")
        # print_map(map)

    gps = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == "[" and map[y][x + 1] == "]":
                gps += 100 * y + x
    print(gps)


part2()
