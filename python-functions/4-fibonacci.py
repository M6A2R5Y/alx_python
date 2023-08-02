#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)

    return fibonacci_list
