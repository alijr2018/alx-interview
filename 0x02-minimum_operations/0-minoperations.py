#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    0. Minimum Operations
    """
    if n <= 1:
        return 0

    # Find the largest factor of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    # If n is a prime number, it can only be achieved by copying and pasting
    return n
