#!/usr/bin/env python3

input = open('day16.txt').read().strip()

HEX2BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


class BITSPacket:
    def __init__(self, bits):
        self.data = bits
        self.version = None
        self.type_id = None
        self.value = None
        self.subpackets = []
        self.length = 0

        self._index = 0
        self._parse()

    def _parse(self):
        self.version = int(self._read_bits(3), 2)
        self.type_id = int(self._read_bits(3), 2)

        if self.type_id == 4:
            # literal value
            self._parse_literal_value()
        else:
            self._parse_operator()
            # sum
            if self.type_id == 0:
                self.value = sum(sub.value for sub in self.subpackets)
            # product
            elif self.type_id == 1:
                self.value = 1
                for sub in self.subpackets:
                    self.value *= sub.value
            # minimum
            elif self.type_id == 2:
                self.value = min(sub.value for sub in self.subpackets)
            # maximum
            elif self.type_id == 3:
                self.value = max(sub.value for sub in self.subpackets)
            # greater than
            elif self.type_id == 5:
                self.value = 1 if self.subpackets[0].value > self.subpackets[1].value else 0
            # less than
            elif self.type_id == 6:
                self.value = 1 if self.subpackets[0].value < self.subpackets[1].value else 0
            # equal to
            elif self.type_id == 7:
                self.value = 1 if self.subpackets[0].value == self.subpackets[1].value else 0

    def _parse_literal_value(self):
        groups = []
        while True:
            bits = self._read_bits(5)
            groups.append(bits[1:])
            if bits[0] == '0':
                break

        self.value = int(''.join(groups), 2)
        self.length = self._index

    def _parse_operator(self):
        length_type_id = int(self._read_bits(1), 2)

        if length_type_id == 0:
            length = int(self._read_bits(15), 2)
            bits = self._read_bits(length)
            while len(bits) > 0:
                packet = BITSPacket(bits)
                self.subpackets.append(packet)
                bits = bits[packet.length:]
            self.length = self._index

        elif length_type_id == 1:
            number = int(self._read_bits(11), 2)
            length = self._index
            bits = self._read_bits()
            for _ in range(number):
                packet = BITSPacket(bits)
                self.subpackets.append(packet)
                bits = bits[packet.length:]
                length += packet.length
            self.length = length

    def _read_bits(self, length=None):
        if length is None:
            bits = self.data[self._index:]
        else:
            bits = self.data[self._index:self._index+length]
        self._index += len(bits)
        return bits


def part1(input):
    bits = ''.join(HEX2BIN[h] for h in input)
    packet = BITSPacket(bits)

    def add_version(packet):
        sum = packet.version
        for sub in packet.subpackets:
            sum += add_version(sub)
        return sum
    return add_version(packet)


def part2(input):
    bits = ''.join(HEX2BIN[h] for h in input)
    packet = BITSPacket(bits)
    return packet.value


if __name__ == '__main__':
    print('--- Day 16: Packet Decoder ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
