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
