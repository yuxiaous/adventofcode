import os

os.chdir(os.path.dirname(__file__))


def input():
    return [int(d) for d in open("input.txt").read().strip()]


def part1():
    disk_map = input()
    disk = []

    # expand data
    id = 0
    for i in range(0, len(disk_map), 2):
        # file
        file_blocks = disk_map[i]
        for _ in range(file_blocks):
            disk.append(id)
        id += 1

        # free space
        if i + 1 < len(disk_map):
            space_blocks = disk_map[i + 1]
            for _ in range(space_blocks):
                disk.append(None)

    # move blocks
    start = 0
    end = len(disk) - 1
    while True:
        while disk[start] != None:
            start += 1
        while disk[end] == None:
            end -= 1
        if start >= end:
            break
        disk[start] = disk[end]
        disk[end] = None

    # calculate filesystem checksum
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == None:
            break
        checksum += i * disk[i]

    print(checksum)


def part2():
    disk_map = input()

    files = {}
    spaces = []

    id = 0
    pos = 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            files[id] = (pos, disk_map[i])
            id += 1
            pos += disk_map[i]
        else:
            spaces.append((pos, disk_map[i]))
            pos += disk_map[i]

    for id in reversed(files.keys()):
        file = files[id]

        for j in range(len(spaces)):
            space = spaces[j]

            if space[0] < file[0] and space[1] >= file[1]:
                files[id] = (space[0], file[1])
                spaces[j] = (space[0] + file[1], space[1] - file[1])
                break

    # calculate filesystem checksum
    checksum = 0
    for id, file in files.items():
        for i in range(file[1]):
            checksum += (file[0] + i) * id
    print(checksum)


part1()
part2()
