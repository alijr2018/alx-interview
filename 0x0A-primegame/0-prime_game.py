#!/usr/bin/python3
"""
0-prime_game.py
"""


def is_prime(num):
    """
    checking is it prime
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    is winner
    """
    wins = {"Maria": 0, "Ben": 0}

    for num in nums:
        primes = generate_primes(num)
        if len(primes) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
