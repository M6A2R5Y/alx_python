#!/usr/bin/python3
for digits in range(10):
    for digits in range(digits + 1, 10):
        print("{:02d}".format(digits * 10 + digits), end=", " if digits < 8 or digits < 9 else "\n",)

