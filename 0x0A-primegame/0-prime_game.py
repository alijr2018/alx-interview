#!/usr/bin/python3
"""
0-prime_game.py
"""


def is_prime(num):
    """
    checking is it prime
    """
    prime_numbers = []
    sieve = [True] * (num + 1)
    for number in range(2, num + 1):
        if sieve[number]:
            prime_numbers.append(number)
            for multiple in range(number, num + 1, number):
                sieve[multiple] = False
    return prime_numbers


def isWinner(x, nums):
    """
    is winner
    """
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for limit in range(x):
        prime_numbers = is_prime(nums[limit])
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
