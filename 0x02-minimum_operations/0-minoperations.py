#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Minimum operations
    """
    if n <= 0:
        return 0

    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0
