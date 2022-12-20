#!/usr/bin/env python3
import re

input = [x for x in open("day07.txt").read().strip().split("\n")]


class FilesystemMeta:
    def __init__(self, type, parent) -> None:
        self.type = type
        self.parent = parent
        self.children = []
        self.size = 0

    def is_file(self):
        return self.type == "file"

    def is_dir(self):
        return self.type == "dir"


class Filesystem:
    def __init__(self) -> None:
        self.filesystem = {"/": FilesystemMeta("dir", None)}

    def parse(self, input: list[str]):
        for line in input:
            if line.startswith("$"):
                match = re.match(r"\$ cd (.+)", line)
                if match:
                    name = match.groups()[0]

                    if name == "/":
                        current = "/"
                    elif name == "..":
                        current = self.filesystem[current].parent
                    else:
                        parent = current
                        current = f"{parent if parent != '/' else ''}/{name}"

            else:
                match = re.match(r"dir (.+)", line)
                if match:
                    name = match.groups()[0]
                    directory = f"{current if current != '/' else ''}/{name}"

                    if directory not in self.filesystem:
                        self.filesystem[directory] = FilesystemMeta("dir", current)

                    if directory not in self.filesystem[current].children:
                        self.filesystem[current].children.append(directory)

                match = re.match(r"(\d+) (.+)", line)
                if match:
                    size = int(match.groups()[0])
                    name = match.groups()[1]
                    filename = f"{current if current != '/' else ''}/{name}"

                    if filename not in self.filesystem:
                        self.filesystem[filename] = FilesystemMeta("file", current)
                        self.filesystem[filename].size = size

                    if filename not in self.filesystem[current].children:
                        self.filesystem[current].children.append(filename)

    def sizeof(self, name):
        meta = self.filesystem[name]

        if meta.is_dir():
            size = 0
            for child in meta.children:
                size += self.sizeof(child)
            return size

        return meta.size

    def dirs(self):
        return [n for n, m in self.filesystem.items() if m.is_dir()]

    def files(self):
        return [n for n, m in self.filesystem.items() if m.is_file()]


filesystem = Filesystem()
filesystem.parse(input)


def part1():
    total = 0
    for name in filesystem.dirs():
        size = filesystem.sizeof(name)
        if size <= 100000:
            total += size
    return total


def part2():
    used = filesystem.sizeof("/")
    unused = 70000000 - used
    required = 30000000 - unused

    sizes = []
    for name in filesystem.dirs():
        size = filesystem.sizeof(name)
        if size > required:
            sizes.append(size)
    return min(sizes)


if __name__ == "__main__":
    print("--- Day 7: No Space Left On Device ---")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
