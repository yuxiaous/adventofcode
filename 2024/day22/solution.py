import os

os.chdir(os.path.dirname(__file__))


def input():
    input = open("input.txt").read().strip()
    secrets = [int(x) for x in input.split("\n")]
    return secrets


def generate(secret):
    secret = ((secret * 0x040) ^ secret) % 0x1000000
    secret = ((secret // 0x20) ^ secret) % 0x1000000
    secret = ((secret * 0x800) ^ secret) % 0x1000000
    return secret


def part1():
    secrets = []
    for secret in input():
        for _ in range(2000):
            secret = generate(secret)
        secrets.append(secret)
    print(sum(secrets))


part1()


def part2():
    bananas = {}

    for secret in input():
        prices = []
        changes = []
        buyer = {}

        prices.append(secret % 10)
        for _ in range(2000):
            secret = generate(secret)
            prices.append(secret % 10)
            changes.append(prices[-1] - prices[-2])

            if len(changes) >= 4:
                seq = tuple(changes[-4:])
                if seq not in buyer:
                    buyer[seq] = prices[-1]

        for seq, price in buyer.items():
            if seq not in bananas:
                bananas[seq] = 0
            bananas[seq] += price

    print(max(bananas.values()))


part2()
