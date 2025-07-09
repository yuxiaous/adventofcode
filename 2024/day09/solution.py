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


part1()
