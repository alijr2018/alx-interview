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


def prime_sieve(n):
    """
    prime
    """
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    is winner
    """
    wins_maria = 0
    wins_ben = 0

    for n in nums:
        primes = prime_sieve(n)
        prime_count = sum(1 for p in primes if p <= n)

        if prime_count % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
