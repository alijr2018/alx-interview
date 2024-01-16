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

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return n
