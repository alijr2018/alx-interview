#!/usr/bin/python3
"""
0-prime_game.py
"""


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_player_win(primes, n):
        memo = {}

        def can_win(count):
            if count <= 1:
                return False
            if count in memo:
                return memo[count]
            for prime in primes:
                if count % prime == 0:
                    if not can_win(count - prime):
                        memo[count] = True
                        return True
            memo[count] = False
            return False

        return can_win(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = calculate_primes(n)
        if can_player_win(primes, n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
