#!/usr/bin/python3
"""Module documentation"""


def minOperations(n: int) -> int:
    """Function documentation"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
