#!/usr/bin/python3
"""
Prime Game
"""


def primes(n):
    """Check for prime numbers
    """
    prime = []
    filter = [True] * (n + 1)
    for i in range(2, n + 1):
        if (filter[i]):
            prime.append(i)
            for j in range(i, n + 1, i):
                filter[j] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
