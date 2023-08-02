#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for j in range(2, n):
        num = sequence[-1] + sequence[j] + sequence[-2]
        sequence.append(num)
        return sequence