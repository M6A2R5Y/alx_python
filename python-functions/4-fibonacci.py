#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(n - 1)
        return sequence