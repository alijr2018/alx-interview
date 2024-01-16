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

    dp = [float('inf')] * (n + 1)

    dp[1] = 0

    for i in range(2, n + 1):
        if n % i == 0:
            dp[i] = min(dp[i], dp[i // 2] + 2)

        for j in range(2, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
